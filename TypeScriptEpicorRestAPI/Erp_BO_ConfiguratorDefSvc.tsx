import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ConfiguratorDefSvc
// Description: ConfiguratorDef Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/$metadata", {
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
   Description: Get ConfiguratorDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorDefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusRow
   */  
export function get_ConfiguratorDefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfiguratorDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ConfiguratorDef item
   Description: Calls GetByID to retrieve the ConfiguratorDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   */  
export function get_ConfiguratorDefs_Company_ConfigID(Company:string, ConfigID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs(" + Company + "," + ConfigID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConfiguratorDef for the service
   Description: Calls UpdateExt to update ConfiguratorDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConfiguratorDefs_Company_ConfigID(Company:string, ConfigID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs(" + Company + "," + ConfigID + ")", {
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
   Summary: Call UpdateExt to delete ConfiguratorDef item
   Description: Call UpdateExt to delete ConfiguratorDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConfiguratorDefs_Company_ConfigID(Company:string, ConfigID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ConfiguratorDefs(" + Company + "," + ConfigID + ")", {
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
   Description: Get PcStatusAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcStatusAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusAttchRow
   */  
export function get_PcStatusAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcStatusAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcStatusAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcStatusAttch item
   Description: Calls GetByID to retrieve the PcStatusAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStatusAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
   */  
export function get_PcStatusAttches_Company_ConfigID_DrawingSeq(Company:string, ConfigID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcStatusAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches(" + Company + "," + ConfigID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcStatusAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcStatusAttch for the service
   Description: Calls UpdateExt to update PcStatusAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcStatusAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcStatusAttches_Company_ConfigID_DrawingSeq(Company:string, ConfigID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches(" + Company + "," + ConfigID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PcStatusAttch item
   Description: Call UpdateExt to delete PcStatusAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcStatusAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcStatusAttches_Company_ConfigID_DrawingSeq(Company:string, ConfigID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStatusAttches(" + Company + "," + ConfigID + "," + DrawingSeq + ")", {
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
   Description: Get PcAudits items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcAudits
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcAuditRow
   */  
export function get_PcAudits(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAuditRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAuditRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcAudits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcAuditRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcAuditRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcAudits(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcAudit item
   Description: Calls GetByID to retrieve the PcAudit item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcAudit
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param ChgDate Desc: ChgDate   Required: True   Allow empty value : True
      @param ChgTime Desc: ChgTime   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcAuditRow
   */  
export function get_PcAudits_Company_PartNum_RevisionNum_ChgDate_ChgTime(Company:string, PartNum:string, RevisionNum:string, ChgDate:string, ChgTime:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcAuditRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits(" + Company + "," + PartNum + "," + RevisionNum + "," + ChgDate + "," + ChgTime + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcAuditRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcAudit for the service
   Description: Calls UpdateExt to update PcAudit. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcAudit
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param ChgDate Desc: ChgDate   Required: True   Allow empty value : True
      @param ChgTime Desc: ChgTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcAuditRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcAudits_Company_PartNum_RevisionNum_ChgDate_ChgTime(Company:string, PartNum:string, RevisionNum:string, ChgDate:string, ChgTime:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits(" + Company + "," + PartNum + "," + RevisionNum + "," + ChgDate + "," + ChgTime + ")", {
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
   Summary: Call UpdateExt to delete PcAudit item
   Description: Call UpdateExt to delete PcAudit item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcAudit
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param RevisionNum Desc: RevisionNum   Required: True   Allow empty value : True
      @param ChgDate Desc: ChgDate   Required: True   Allow empty value : True
      @param ChgTime Desc: ChgTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcAudits_Company_PartNum_RevisionNum_ChgDate_ChgTime(Company:string, PartNum:string, RevisionNum:string, ChgDate:string, ChgTime:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcAudits(" + Company + "," + PartNum + "," + RevisionNum + "," + ChgDate + "," + ChgTime + ")", {
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
   Description: Get PcDocRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDocRules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDocRulesRow
   */  
export function get_PcDocRules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDocRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDocRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDocRule item
   Description: Calls GetByID to retrieve the PcDocRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDocRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
   */  
export function get_PcDocRules_Company_ConfigID_RuleSeq(Company:string, ConfigID:string, RuleSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDocRulesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules(" + Company + "," + ConfigID + "," + RuleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDocRulesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDocRule for the service
   Description: Calls UpdateExt to update PcDocRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDocRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDocRulesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDocRules_Company_ConfigID_RuleSeq(Company:string, ConfigID:string, RuleSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules(" + Company + "," + ConfigID + "," + RuleSeq + ")", {
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
   Summary: Call UpdateExt to delete PcDocRule item
   Description: Call UpdateExt to delete PcDocRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDocRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDocRules_Company_ConfigID_RuleSeq(Company:string, ConfigID:string, RuleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRules(" + Company + "," + ConfigID + "," + RuleSeq + ")", {
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
   Description: Get PcDocRulesExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDocRulesExprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDocRulesExprRow
   */  
export function get_PcDocRulesExprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDocRulesExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDocRulesExprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDocRulesExpr item
   Description: Calls GetByID to retrieve the PcDocRulesExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDocRulesExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
   */  
export function get_PcDocRulesExprs_Company_ConfigID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, RuleSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDocRulesExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs(" + Company + "," + ConfigID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDocRulesExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDocRulesExpr for the service
   Description: Calls UpdateExt to update PcDocRulesExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDocRulesExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDocRulesExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDocRulesExprs_Company_ConfigID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, RuleSeq:string, TypeCode:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs(" + Company + "," + ConfigID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcDocRulesExpr item
   Description: Call UpdateExt to delete PcDocRulesExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDocRulesExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDocRulesExprs_Company_ConfigID_RuleSeq_TypeCode_SeqNum(Company:string, ConfigID:string, RuleSeq:string, TypeCode:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocRulesExprs(" + Company + "," + ConfigID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Description: Get PcDocVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDocVars
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDocVarRow
   */  
export function get_PcDocVars(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDocVars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDocVars(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDocVar item
   Description: Calls GetByID to retrieve the PcDocVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDocVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param VarNum Desc: VarNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
   */  
export function get_PcDocVars_Company_ConfigID_VarNum(Company:string, ConfigID:string, VarNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDocVarRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars(" + Company + "," + ConfigID + "," + VarNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDocVarRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDocVar for the service
   Description: Calls UpdateExt to update PcDocVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDocVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param VarNum Desc: VarNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDocVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDocVars_Company_ConfigID_VarNum(Company:string, ConfigID:string, VarNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars(" + Company + "," + ConfigID + "," + VarNum + ")", {
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
   Summary: Call UpdateExt to delete PcDocVar item
   Description: Call UpdateExt to delete PcDocVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDocVar
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param VarNum Desc: VarNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDocVars_Company_ConfigID_VarNum(Company:string, ConfigID:string, VarNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcDocVars(" + Company + "," + ConfigID + "," + VarNum + ")", {
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
   Description: Get PcInputs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   */  
export function get_PcInputs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInput item
   Description: Calls GetByID to retrieve the PcInput item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInput
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   */  
export function get_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInput for the service
   Description: Calls UpdateExt to update PcInput. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInput
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
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
   Summary: Call UpdateExt to delete PcInput item
   Description: Call UpdateExt to delete PcInput item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInput
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
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
   Description: Get PcStrComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcStrComps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStrCompRow
   */  
export function get_PcStrComps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStrCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStrCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcStrComps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcStrComps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcStrComp item
   Description: Calls GetByID to retrieve the PcStrComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStrComp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PosOrder Desc: PosOrder   Required: True
      @param CompName Desc: CompName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
   */  
export function get_PcStrComps_Company_ConfigID_PosOrder_CompName(Company:string, ConfigID:string, PosOrder:string, CompName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcStrCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps(" + Company + "," + ConfigID + "," + PosOrder + "," + CompName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcStrCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcStrComp for the service
   Description: Calls UpdateExt to update PcStrComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcStrComp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PosOrder Desc: PosOrder   Required: True
      @param CompName Desc: CompName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStrCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcStrComps_Company_ConfigID_PosOrder_CompName(Company:string, ConfigID:string, PosOrder:string, CompName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps(" + Company + "," + ConfigID + "," + PosOrder + "," + CompName + ")", {
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
   Summary: Call UpdateExt to delete PcStrComp item
   Description: Call UpdateExt to delete PcStrComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcStrComp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PosOrder Desc: PosOrder   Required: True
      @param CompName Desc: CompName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcStrComps_Company_ConfigID_PosOrder_CompName(Company:string, ConfigID:string, PosOrder:string, CompName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcStrComps(" + Company + "," + ConfigID + "," + PosOrder + "," + CompName + ")", {
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
   Description: Get PcTargetEntities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcTargetEntities
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcTargetEntityRow
   */  
export function get_PcTargetEntities(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcTargetEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcTargetEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcTargetEntities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcTargetEntities(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcTargetEntity item
   Description: Calls GetByID to retrieve the PcTargetEntity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcTargetEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
   */  
export function get_PcTargetEntities_Company_ConfigID_TableName(Company:string, ConfigID:string, TableName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcTargetEntityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities(" + Company + "," + ConfigID + "," + TableName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcTargetEntityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcTargetEntity for the service
   Description: Calls UpdateExt to update PcTargetEntity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcTargetEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcTargetEntityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcTargetEntities_Company_ConfigID_TableName(Company:string, ConfigID:string, TableName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities(" + Company + "," + ConfigID + "," + TableName + ")", {
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
   Summary: Call UpdateExt to delete PcTargetEntity item
   Description: Call UpdateExt to delete PcTargetEntity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcTargetEntity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TableName Desc: TableName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcTargetEntities_Company_ConfigID_TableName(Company:string, ConfigID:string, TableName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PcTargetEntities(" + Company + "," + ConfigID + "," + TableName + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePcStatus:string, whereClausePcStatusAttch:string, whereClausePcAudit:string, whereClausePcDocRules:string, whereClausePcDocRulesExpr:string, whereClausePcDocVar:string, whereClausePcInputs:string, whereClausePcStrComp:string, whereClausePcTargetEntity:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcStatus!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcStatus=" + whereClausePcStatus
   }
   if(typeof whereClausePcStatusAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcStatusAttch=" + whereClausePcStatusAttch
   }
   if(typeof whereClausePcAudit!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcAudit=" + whereClausePcAudit
   }
   if(typeof whereClausePcDocRules!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDocRules=" + whereClausePcDocRules
   }
   if(typeof whereClausePcDocRulesExpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDocRulesExpr=" + whereClausePcDocRulesExpr
   }
   if(typeof whereClausePcDocVar!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDocVar=" + whereClausePcDocVar
   }
   if(typeof whereClausePcInputs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputs=" + whereClausePcInputs
   }
   if(typeof whereClausePcStrComp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcStrComp=" + whereClausePcStrComp
   }
   if(typeof whereClausePcTargetEntity!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcTargetEntity=" + whereClausePcTargetEntity
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetRows" + params, {
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
export function get_GetByID(configID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof configID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "configID=" + configID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetList" + params, {
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
   Summary: Invoke method GetFormatString
   Description: Get the format string for a PcInput
   OperationID: GetFormatString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFormatString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFormatString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFormatString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetFormatString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInputPossibleValues
   Description: Get the values from Radio and DropDownList
   OperationID: GetInputPossibleValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInputPossibleValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInputPossibleValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInputPossibleValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetInputPossibleValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailInputs
   Description: Get the available inputs that may be used to build smart string.
   OperationID: GetAvailInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetAvailInputs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildSampleSmartString
   Description: Updates the PcStatus Sample Smart String when the smart string parameters are changed.
   OperationID: BuildSampleSmartString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildSampleSmartString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildSampleSmartString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildSampleSmartString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/BuildSampleSmartString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SalesKitConfiguration
   Description: If a partplant record is available for the current plant then check the SourceType
If not partplant available then check the typecode on the part record.
   OperationID: SalesKitConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesKitConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesKitConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SalesKitConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/SalesKitConfiguration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SmartStringMoveDown
   Description: Move a smart string input down in the available inputs list
   OperationID: SmartStringMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SmartStringMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SmartStringMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SmartStringMoveDown(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/SmartStringMoveDown", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SmartStringMoveUp
   Description: Move a smart string input up in the selected inputs list
   OperationID: SmartStringMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SmartStringMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SmartStringMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SmartStringMoveUp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/SmartStringMoveUp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SyncRevision
   Description: This method synchronizes the part revision approval flag when the PcStatus.Approved
flag changes
   OperationID: SyncRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SyncRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyncRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SyncRevision(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/SyncRevision", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdatePcStruct
   Description: Update PcStruct records with new display sequence
   OperationID: UpdatePcStruct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePcStruct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePcStruct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePcStruct(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/UpdatePcStruct", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateConfigSequence
   Description: Called prior to testing input/rules to generate
           configuration sequence records
   OperationID: GenerateConfigSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateConfigSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateConfigSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateConfigSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GenerateConfigSequence", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteConfigSequence
   Description: Called after testing inputs/rules to delete configuration
           sequence records
   OperationID: DeleteConfigSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteConfigSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteConfigSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteConfigSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DeleteConfigSequence", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSpecRevs
   Description: Get the valid specification revisions
   OperationID: GetSpecRevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSpecRevs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSpecRevs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSpecRevs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetSpecRevs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLinkedParts
   Description: Get a list of parts that are related to this configuration id
   OperationID: GetLinkedParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLinkedParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLinkedParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLinkedParts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetLinkedParts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckValidRevision
   Description: verify the selected revision is valid
   OperationID: CheckValidRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckValidRevision(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/CheckValidRevision", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckConfigAndGetType
   Description: Check if Configuration exists and return ConfigType in case exist
   OperationID: CheckConfigAndGetType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckConfigAndGetType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckConfigAndGetType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckConfigAndGetType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/CheckConfigAndGetType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevisions
   Description: Get a list of revisions that are related to the selected part number
   OperationID: GetRevisions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevisions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevisions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetRevisions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEffectiveRevision
   Description: Get the latest effective revision for the related part number and configuration id
   OperationID: GetEffectiveRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEffectiveRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEffectiveRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetEffectiveRevision(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetEffectiveRevision", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetConfigurationOptions
   Description: Get the valid options that are used for populating configuration design options.  This will populate the ConfigPartCreateMethod, ConfigSmartStringStyle,
   OperationID: GetConfigurationOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConfigurationOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfigurationOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetConfigurationOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetConfigurationOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTargetTables
   Description: Get the valid table options for config type
   OperationID: GetTargetTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTargetTables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetTargetTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
validated by the ValidatePassword method in UserFile BO.  Run this before SyncRevision method is called.
   OperationID: PromptForPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromptForPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PromptForPassword(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PromptForPassword", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangingEntConf
   Description: This methods checks to see if any enterprise configurator specific settings
have been created.  If so then a message should be displayed prior to unchecking
the enterprise configurator checkbox
   OperationID: ChangingEntConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingEntConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingEntConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangingEntConf(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ChangingEntConf", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePcStatus
   Description: Create a new configuration for a Part Revision
   OperationID: CreatePcStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePcStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePcStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePcStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/CreatePcStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSequenceForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
ALL ALTERNATES OF THE PARTREVISION WILL BE RETURNED if ipcomplete is true
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
   OperationID: GetSequenceForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSequenceForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSequenceForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSequenceForTree(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetSequenceForTree", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshSubConf
   Description: This method rebuilds the configurator sequence. It's
a compilation of all sub configured parts defined in the method of manufacture
for the parent configured part.
   OperationID: RefreshSubConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshSubConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshSubConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshSubConf(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/RefreshSubConf", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshConfiguratorSequence
   Description: This method rebuilds the configurator sequence and updates the PcValueHead table to apply the new sequence to existing configurations.
   OperationID: RefreshConfiguratorSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshConfiguratorSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshConfiguratorSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshConfiguratorSequence(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/RefreshConfiguratorSequence", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshPcStatusBeforeDisapprove
   Description: Refresh PcStatus when RegenConfig is True before disapproving in case the record has been changed by the Regenerate Configurator process already.
   OperationID: RefreshPcStatusBeforeDisapprove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshPcStatusBeforeDisapprove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshPcStatusBeforeDisapprove_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshPcStatusBeforeDisapprove(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/RefreshPcStatusBeforeDisapprove", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocRulesMoveDown
   Description: Move a document rule down in the order of configuration rules.
   OperationID: DocRulesMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocRulesMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocRulesMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocRulesMoveDown(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DocRulesMoveDown", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocRulesMoveUp
   Description: Move a document rule up in the order of configuration rules.
   OperationID: DocRulesMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocRulesMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocRulesMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocRulesMoveUp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DocRulesMoveUp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeConfigType
   Description: The default value for Product Configurator types is true for displaying the summary screen.  For all other types it is false because it is not allowed.
   OperationID: OnChangeConfigType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeConfigType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeConfigType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeConfigType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangeConfigType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAttrClassID
   Description: Validate if exists the Part Attribute Class selected and if the Inputs have attributes assigned.
   OperationID: OnChangeAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttrClassID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangeAttrClassID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedDocRuleCompany
   Description: Change Company when click check boxes for Multi-Company or Local company
Must clear the list of companies in case already selected in picker list
   OperationID: OnChangedDocRuleCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedDocRuleCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedDocRuleCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedDocRuleCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedDocRuleCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcDocRulesExprExprType
   Description: This method is executed when changing the ExprType column of PcDocRulesExpr, it is used to clear all fields related with
action expression
   OperationID: OnChangedPcDocRulesExprExprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocRulesExprExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocRulesExprExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcDocRulesExprExprType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedPcDocRulesExprExprType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcDocRulesRuleType
   Description: This method is executed when changing the RuleType column of PcDocRules, it is used to clear all fields related with
condition expression
   OperationID: OnChangedPcDocRulesRuleType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocRulesRuleType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocRulesRuleType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcDocRulesRuleType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedPcDocRulesRuleType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePcDocRulesExprLValue
   Description: This method is executed when changing the LValue column of PcDocRulesExpr, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcDocRulesExprLValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcDocRulesExprLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcDocRulesExprLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePcDocRulesExprLValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangePcDocRulesExprLValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePcDocRulesLValue
   Description: This method is executed when changing the LValue column of PcDocRules, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcDocRulesLValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcDocRulesLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcDocRulesLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePcDocRulesLValue(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangePcDocRulesLValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcStatusRemoveLink
   Description: Only when Part Creation is enabled should add the part table to target entity list
   OperationID: OnChangedPcStatusRemoveLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcStatusRemoveLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcStatusRemoveLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcStatusRemoveLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedPcStatusRemoveLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcStatusCreatePart
   Description: Only when Part Creation is enabled should add the part table to target entity list
   OperationID: OnChangedPcStatusCreatePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcStatusCreatePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcStatusCreatePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcStatusCreatePart(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedPcStatusCreatePart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePcStatusKBConfigID
   Description: On change of the CPQ Configurator ID
   OperationID: OnChangePcStatusKBConfigID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcStatusKBConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcStatusKBConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePcStatusKBConfigID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangePcStatusKBConfigID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetKBConfigSearchList
   Description: Get a list of CPQ Configurators
   OperationID: Get_GetKBConfigSearchList
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKBConfigSearchList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetKBConfigSearchList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetKBConfigSearchList" + params, {
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
   Summary: Invoke method GetPcTargetEntityList
   Description: Gets a list of PcTargetEntity records based on a where clause.
   OperationID: GetPcTargetEntityList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPcTargetEntityList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPcTargetEntityList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPcTargetEntityList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetPcTargetEntityList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPcTargetEntityListIncludeUD
   Description: Gets a list of PcTargetEntity records based on a where clause.
   OperationID: GetPcTargetEntityListIncludeUD
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPcTargetEntityListIncludeUD_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPcTargetEntityListIncludeUD_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPcTargetEntityListIncludeUD(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetPcTargetEntityListIncludeUD", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePcDocRulesDelete
   Description: Validate if exist child record when try to delete
   OperationID: ValidatePcDocRulesDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcDocRulesDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcDocRulesDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePcDocRulesDelete(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ValidatePcDocRulesDelete", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EditorFilter
   Description: Return filter for editor
   OperationID: EditorFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EditorFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EditorFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EditorFilter(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/EditorFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportConfiguration
   Description: Exports a configurator.
   OperationID: ExportConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ExportConfiguration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeployToEWC
   Description: Export the client side portions of the configurator for EWC to use when constructing their UI
   OperationID: DeployToEWC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeployToEWC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeployToEWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeployToEWC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DeployToEWC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrievePcLayeredImagesForExport
   Description: retrieve layered image inputs for export when advanced configurator
   OperationID: RetrievePcLayeredImagesForExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrievePcLayeredImagesForExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrievePcLayeredImagesForExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrievePcLayeredImagesForExport(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/RetrievePcLayeredImagesForExport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportConfiguration
   Description: Imports the Configuration records for kinetic and non kientic
   OperationID: ImportConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/ImportConfiguration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingPcDocVarDataType
   Description: Validate variable is not being used.
   OperationID: OnChangingPcDocVarDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPcDocVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcDocVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingPcDocVarDataType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangingPcDocVarDataType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcDocVarDataType
   Description: Clean DataType when dataType is changed
   OperationID: OnChangedPcDocVarDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcDocVarDataType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedPcDocVarDataType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingPcDocVarVarName
   Description: Validate Changing VarName
   OperationID: OnChangingPcDocVarVarName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPcDocVarVarName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcDocVarVarName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingPcDocVarVarName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangingPcDocVarVarName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedPcDocVarExprType
   Description: This method is executed when changing the ExprType column of PcDocVar, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcDocVarExprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcDocVarExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcDocVarExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedPcDocVarExprType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedPcDocVarExprType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocVarMoveDown
   Description: Move a Variable down in the order of document variables.
   OperationID: DocVarMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocVarMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocVarMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocVarMoveDown(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DocVarMoveDown", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DocVarMoveUp
   Description: Move a Variable up in the order of document variables.
   OperationID: DocVarMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocVarMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocVarMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocVarMoveUp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DocVarMoveUp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailDocVariables
   Description: Get the available document variables that may be used in code editor.
   OperationID: GetAvailDocVariables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailDocVariables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailDocVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailDocVariables(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetAvailDocVariables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildCodeEditorInputs
   Description: builds list of inputs used in this config that are needed by the code editor available selections panel
   OperationID: BuildCodeEditorInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCodeEditorInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCodeEditorInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildCodeEditorInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/BuildCodeEditorInputs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeEditorOptions
   Description: this method populates the code editor options that are database dependent
   OperationID: GetCodeEditorOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeEditorOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeEditorOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeEditorOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetCodeEditorOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTargetEntityColumns
   Description: retrieve TargetEntity Columns
   OperationID: GetTargetEntityColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTargetEntityColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTargetEntityColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTargetEntityColumns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetTargetEntityColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedEntityColumn
   Description: validate if exists the selected entity column in the specify result set
   OperationID: OnChangedEntityColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedEntityColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedEntityColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedEntityColumn(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/OnChangedEntityColumn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateConfiguration
   Description: Duplicates configuration. It won't duplicate Method Rules, Method Variables, Lookup Tables (Definition), Sequence, Global Variables(Definition), Images(Definition), Memos, Change Log
   OperationID: DuplicateConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DuplicateConfiguration", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckForEpicorWebClientSyncUpdates
   Description: Call this method to determine whether or the configuration definition has changed since the last time the configurator was generated in EWC.
   OperationID: CheckForEpicorWebClientSyncUpdates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForEpicorWebClientSyncUpdates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForEpicorWebClientSyncUpdates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForEpicorWebClientSyncUpdates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/CheckForEpicorWebClientSyncUpdates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateEpicorWebDeployStatus
   Description: Call this method after the configuration has been successfully generated in EWC.
   OperationID: UpdateEpicorWebDeployStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateEpicorWebDeployStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateEpicorWebDeployStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateEpicorWebDeployStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/UpdateEpicorWebDeployStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestInputsPostDeployMessageToEWC
   Description: Called when user is executed Test Inputs for an EWC configurator
   OperationID: TestInputsPostDeployMessageToEWC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestInputsPostDeployMessageToEWC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestInputsPostDeployMessageToEWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestInputsPostDeployMessageToEWC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/TestInputsPostDeployMessageToEWC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostDeployMessageToEWC
   Description: Method to call when EWC is to execute their logic to deploy a configurator to EWC and generate all of the necessary files.
   OperationID: PostDeployMessageToEWC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostDeployMessageToEWC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostDeployMessageToEWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostDeployMessageToEWC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/PostDeployMessageToEWC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcStatus
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcStatus", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcStatusAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatusAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatusAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatusAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcStatusAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcStatusAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcAudit
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcAudit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcAudit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcAudit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcAudit(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcAudit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcDocRules
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDocRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDocRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDocRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDocRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcDocRules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcDocRulesExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDocRulesExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDocRulesExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDocRulesExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDocRulesExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcDocRulesExpr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcDocVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDocVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDocVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDocVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDocVar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcDocVar", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcInputs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcInputs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcStrComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStrComp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStrComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStrComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcStrComp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcStrComp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPcTargetEntity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcTargetEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcTargetEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcTargetEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcTargetEntity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetNewPcTargetEntity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorDefSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcAuditRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcAuditRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesExprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDocRulesExprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocRulesRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDocRulesRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDocVarRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDocVarRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStatusAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStatusListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStatusRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStrCompRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStrCompRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcTargetEntityRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcTargetEntityRow[],
}

export interface Erp_Tablesets_PcAuditRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  System Date when this change was made.  */  
   "ChgDate":string,
      /**  System Time (seconds since midnight) of when the changes were made.  */  
   "ChgTime":number,
      /**  UserID who made the changes.  Not maintainable by the user.  */  
   "ChgBy":string,
      /**  Used to enter a description of the changes that were made.  */  
   "ChgDescription":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CanUpdate":boolean,
   "CvtChgTime":string,
   "BitFlag":number,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcDocRulesExprRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Part Number of the associated configurator  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  Document Rule Sequence Number  */  
   "RuleSeq":number,
      /**  Sequence Number.  */  
   "SeqNum":number,
      /**  Document Rule Expression  */  
   "Expression":string,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ProcessOrder  */  
   "ProcessOrder":number,
      /**  ExprType  */  
   "ExprType":string,
      /**  LValue  */  
   "LValue":string,
      /**  CompareOpr  */  
   "CompareOpr":string,
      /**  RValue  */  
   "RValue":string,
      /**  RValueType  */  
   "RValueType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DispActionString":string,
   "dbTable":string,
   "dbField":string,
      /**  Assing the default format for the constant editor  */  
   "Format":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcDocRulesRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  Part Number of the associated configurator  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  External Company ID  */  
   "ExtCompanyID":string,
      /**  Document Rule Sequence Number  */  
   "RuleSeq":number,
      /**  Document Rule String  */  
   "RuleString":string,
      /**  Document Rule Type  */  
   "RuleType":string,
      /**  Name for the calculated field  */  
   "CalcName":string,
      /**  Calculated field data type  */  
   "CalcDataType":string,
      /**  Database field  */  
   "dbField":string,
      /**  Database table  */  
   "dbTable":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  Comment  */  
   "Comments":string,
      /**  Document Rule Expression  */  
   "RuleExpr":string,
      /**  Process Sequence  */  
   "ProcessSeq":number,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  LValue  */  
   "LValue":string,
      /**  CompareOpr  */  
   "CompareOpr":string,
      /**  RValue  */  
   "RValue":string,
      /**  RValueType  */  
   "RValueType":string,
      /**  Description  */  
   "Description":string,
      /**  ExtCompanyList  */  
   "ExtCompanyList":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "dspRuleType":string,
   "EntprsConf":boolean,
   "TypeCode":string,
   "CanUpdate":boolean,
   "CompanyName":string,
   "dspdbField":string,
   "dspdbTable":string,
      /**  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  */  
   "MultiCompany":boolean,
      /**  Assing the default format for the constant editor  */  
   "Format":string,
   "DispLinkString":string,
   "BitFlag":number,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumSalesUM":string,
   "PartNumSellingFactor":number,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcDocVarRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  VarNum  */  
   "VarNum":number,
      /**  VarName  */  
   "VarName":string,
      /**  DataType  */  
   "DataType":string,
      /**  Expression  */  
   "Expression":string,
      /**  ExprType  */  
   "ExprType":string,
      /**  VarSeq  */  
   "VarSeq":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "Format":string,
   "CanUpdate":boolean,
   "DispLinkString":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   "InputName":string,
      /**  The order that the tab function will step through the inputs.  */  
   "TabOrder":number,
      /**  The type of data that can be stored in the control.  */  
   "DataType":string,
      /**  The format for which the data will be stored.  */  
   "FormatString":string,
      /**  The initial value for the control.  */  
   "InitVal":string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   "StatusText":string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   "Required":boolean,
      /**  On what page does the control exist.  */  
   "PageSeq":number,
      /**  The control's label.  */  
   "SideLabel":string,
      /**  The pixel position for the x axis.  */  
   "xPos":number,
      /**  The pixel position for the Y axis.  */  
   "yPos":number,
      /**  The pixel width of the control.  */  
   "pWidth":number,
      /**  The pixel height of the control.  */  
   "pHeight":number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   "ControlType":string,
      /**  The prompt when expression for the widget.  */  
   "PromptWhen":string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   "ListItems":string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   "StartDec":number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   "EndDec":number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   "IncrPrec":number,
      /**  The starting date for a validated date fill-in.  */  
   "StartDate":string,
      /**  The ending date for a validated date fill-in.  */  
   "EndDate":string,
      /**  The list of valid responses for a validated string input.  */  
   "ValList":string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   "Horizontal":boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   "IsGlobal":boolean,
      /**  The On Leave expression for the control.  */  
   "OnLeave":string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   "WebInputName":string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   "SummaryLabel":string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   "DLRunProgram":boolean,
      /**  The Progress program used for building a dynamic list.  */  
   "DLProgramName":string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   "DLProgramInputs":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   "HideInSummary":boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   "OnLeave2":string,
      /**  If true, the input will not be displayed on the input page  */  
   "Invisible":boolean,
      /**  Comments describing the input  */  
   "Comments":string,
      /**  Global Input Variable  */  
   "GlobalInputVar":boolean,
      /**  Global Input Variable Name  */  
   "GlbInputVarName":string,
      /**  Do not display input in Summary  */  
   "NoDispSummary":boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   "ExternalRef":boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   "AttributeID":string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMinValue":boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMaxValue":boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseIncrValue":boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseInitVal":boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   "UseToolTip":boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseScreenLabel":boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseListValues":boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   "SmartPartSeq":number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   "SmartStringStart":number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   "SmartStringEnd":number,
      /**  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  */  
   "ShowDistinct":boolean,
      /**  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  */  
   "DesignControlType":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ReadOnly  */  
   "ReadOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AutoSizeList  */  
   "AutoSizeList":boolean,
      /**  ListWidth  */  
   "ListWidth":number,
      /**  ImageSource  */  
   "ImageSource":string,
      /**  ImageLayerID  */  
   "ImageLayerID":string,
   "AllowSmartString":boolean,
   "AttributeDescription":string,
      /**  If true then fields on the record may be updated  */  
   "CanUpdate":boolean,
   "Content":string,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   "DispCharVal":string,
   "DspPageSeq":number,
      /**  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  */  
   "FullInputName":string,
   "ImageMapping":boolean,
      /**  The initial value of a date field  */  
   "InitDate":string,
      /**  The initial value of a decimal input  */  
   "InitDecimal":number,
      /**  The initial value for a logical input  */  
   "InitLogical":boolean,
      /**  Indicates whether or not Input Rules have been defined.  */  
   "InputRules":boolean,
      /**  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  */  
   "InputType":string,
   "IsGlobalInputVar":boolean,
   "OnLaunch":string,
   "PageDisplaySeq":number,
      /**  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  */  
   "PcDynLstCount":number,
   "ReadOnlyExpression":string,
   "TestPlan":boolean,
   "ImageURL":string,
   "BitFlag":number,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcStatusAttchRow{
   "Company":string,
   "ConfigID":string,
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

export interface Erp_Tablesets_PcStatusListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number.  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  Configurator Approval Status  */  
   "Approved":boolean,
      /**  Date the configuration was approved.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Smart String Style  */  
   "StringStyle":string,
      /**  Smart String Seperator character  */  
   "Separator":string,
      /**  Smart String Digit Structure  */  
   "NumberFormat":string,
      /**  Smart String Starting Sequence  */  
   "StartNumber":number,
      /**  Part Creation Method  */  
   "CrtCustPart":boolean,
      /**  Smart String preface with part numbner  */  
   "PrefacePart":boolean,
      /**  Configurator Version  */  
   "ConfigVersion":number,
      /**  Quote Price Code  */  
   "QuotePCode":string,
      /**  Order Price Code  */  
   "OrderPCode":string,
      /**  OrdQuoCom  */  
   "OrdQuoCom":boolean,
      /**  JobPickCom  */  
   "JobPickCom":boolean,
      /**  ShipCom  */  
   "ShipCom":boolean,
      /**  InvCom  */  
   "InvCom":boolean,
      /**  Create Part Flag  */  
   "CreatePart":boolean,
      /**  Create part method  */  
   "CrtPartUsing":string,
      /**  Create New Part In Quote Entry  */  
   "InQuoting":boolean,
      /**  Automatically create a new part number  */  
   "AutoCrtPart":boolean,
      /**  Do not prompt user if part exists  */  
   "NotUnique":boolean,
      /**  Create New Part In Sales Order Entry  */  
   "InOrderEntry":boolean,
      /**  Create New Part In Job Entry  */  
   "InJobEntry":boolean,
      /**  Create Bill of Material  */  
   "CreateBOM":boolean,
      /**  Create Part at zero cost  */  
   "ZeroCost":boolean,
      /**  Create Smart String in part description  */  
   "CrtPartDesc":boolean,
      /**  File Name  */  
   "FileName":string,
      /**  Added to provide backward compatibility to previous releases.  */  
   "SingleLevelConf":boolean,
      /**  Indicates if the input values should be saved.  */  
   "SaveInputValues":boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   "SetPartNumOnly":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   "AprvRev":boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   "EntprsConf":boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   "Synchronize":boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   "DispConfSummary":boolean,
      /**  Part creation comments  */  
   "PartComments":string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   "CompPricing":boolean,
      /**  External configurator  */  
   "ExtConfig":boolean,
      /**  External company ID  */  
   "ExtMfgCompID":string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   "TestPlan":boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   "MarkMtlGlb":boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   "SIValuesUseQt":boolean,
      /**  This field will enable smart string processing for this configuration  */  
   "AllowSmartString":boolean,
   "InDemandEntry":boolean,
      /**  Demand Price Code  */  
   "DemandPCode":string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   "AllAltMethods":boolean,
      /**  SIValuesUseGenMethod  */  
   "SIValuesUseGenMethod":boolean,
      /**  Description  */  
   "Description":string,
      /**  ConfigType  */  
   "ConfigType":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ShrinkFieldProperties  */  
   "ShrinkFieldProperties":boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   "AuditDesc":string,
      /**  A sample smart string constructed from the smart string options  */  
   "SampleSmartString":string,
      /**  The available inputs available for use in the smart string  */  
   "AvailSmartStringInputs":string,
      /**  The inputs that have been selected for use in the smart string  */  
   "SelectedSmartStringInputs":string,
      /**  True if the PartRev record is approved  */  
   "RevApproved":boolean,
      /**  If true then detail fields other than Approved can be updated  */  
   "CanUpdate":boolean,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   "ECOGroup":string,
   "IsValidPwd":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcStatusRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number.  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  Configurator Approval Status  */  
   "Approved":boolean,
      /**  Date the configuration was approved.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Smart String Style  */  
   "StringStyle":string,
      /**  Smart String Seperator character  */  
   "Separator":string,
      /**  Smart String Digit Structure  */  
   "NumberFormat":string,
      /**  Smart String Starting Sequence  */  
   "StartNumber":number,
      /**  Part Creation Method  */  
   "CrtCustPart":boolean,
      /**  Smart String preface with part numbner  */  
   "PrefacePart":boolean,
      /**  Configurator Version  */  
   "ConfigVersion":number,
      /**  Quote Price Code  */  
   "QuotePCode":string,
      /**  Order Price Code  */  
   "OrderPCode":string,
      /**  OrdQuoCom  */  
   "OrdQuoCom":boolean,
      /**  JobPickCom  */  
   "JobPickCom":boolean,
      /**  ShipCom  */  
   "ShipCom":boolean,
      /**  InvCom  */  
   "InvCom":boolean,
      /**  Create Part Flag  */  
   "CreatePart":boolean,
      /**  Create part method  */  
   "CrtPartUsing":string,
      /**  Create New Part In Quote Entry  */  
   "InQuoting":boolean,
      /**  Automatically create a new part number  */  
   "AutoCrtPart":boolean,
      /**  Do not prompt user if part exists  */  
   "NotUnique":boolean,
      /**  Create New Part In Sales Order Entry  */  
   "InOrderEntry":boolean,
      /**  Create New Part In Job Entry  */  
   "InJobEntry":boolean,
      /**  Create Bill of Material  */  
   "CreateBOM":boolean,
      /**  Create Part at zero cost  */  
   "ZeroCost":boolean,
      /**  Create Smart String in part description  */  
   "CrtPartDesc":boolean,
      /**  File Name  */  
   "FileName":string,
      /**  Added to provide backward compatibility to previous releases.  */  
   "SingleLevelConf":boolean,
      /**  Indicates if the input values should be saved.  */  
   "SaveInputValues":boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   "SetPartNumOnly":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   "AprvRev":boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   "EntprsConf":boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   "Synchronize":boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   "DispConfSummary":boolean,
      /**  Part creation comments  */  
   "PartComments":string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   "CompPricing":boolean,
      /**  External configurator  */  
   "ExtConfig":boolean,
      /**  External company ID  */  
   "ExtMfgCompID":string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   "TestPlan":boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   "MarkMtlGlb":boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   "SIValuesUseQt":boolean,
      /**  This field will enable smart string processing for this configuration  */  
   "AllowSmartString":boolean,
   "InDemandEntry":boolean,
      /**  Demand Price Code  */  
   "DemandPCode":string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   "AllAltMethods":boolean,
      /**  AllowReconPO  */  
   "AllowReconPO":boolean,
      /**  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  */  
   "CompPricingJobMethod":boolean,
      /**  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  */  
   "CreateRev":boolean,
      /**  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  */  
   "DefaultECO":string,
      /**  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  */  
   "GenerateMethod":boolean,
      /**  PromptForConfig  */  
   "PromptForConfig":boolean,
      /**  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  */  
   "PromptForCheckout":boolean,
      /**  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  */  
   "RemoveLink":boolean,
      /**  SIValuesUseGenMethod  */  
   "SIValuesUseGenMethod":boolean,
      /**  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  */  
   "UseSavedLayout":boolean,
      /**  Description  */  
   "Description":string,
      /**  ConfigType  */  
   "ConfigType":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  RegenConfig  */  
   "RegenConfig":boolean,
      /**  CreateNewConfigID  */  
   "CreateNewConfigID":boolean,
      /**  UseTemplatePartDefaults  */  
   "UseTemplatePartDefaults":boolean,
      /**  DefaultPartNum  */  
   "DefaultPartNum":string,
      /**  DefaultRevisionNum  */  
   "DefaultRevisionNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  */  
   "AttrClassID":string,
      /**  RecycleJobs  */  
   "RecycleJobs":boolean,
      /**  ClientDeployedToEWCDate  */  
   "ClientDeployedToEWCDate":string,
      /**  EWCClientSyncRequired  */  
   "EWCClientSyncRequired":boolean,
      /**  ShrinkFieldProperties  */  
   "ShrinkFieldProperties":boolean,
      /**  Kinetic  */  
   "Kinetic":boolean,
      /**  KBConfigID  */  
   "KBConfigID":number,
      /**  KBConfigDesc  */  
   "KBConfigDesc":string,
      /**  The available inputs available for use in the smart string  */  
   "AvailSmartStringInputs":string,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   "ECOGroup":string,
      /**  Indicates if the configurator has inputs in its design.  */  
   "HasInputs":boolean,
   "IsValidPwd":boolean,
      /**  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  */  
   "ResetPCInputsAttributes":boolean,
      /**  True if the PartRev record is approved  */  
   "RevApproved":boolean,
      /**  A sample smart string constructed from the smart string options  */  
   "SampleSmartString":string,
      /**  The inputs that have been selected for use in the smart string  */  
   "SelectedSmartStringInputs":string,
      /**  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  */  
   "UpdateCreatePartTarget":boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   "AuditDesc":string,
      /**  If true then detail fields other than Approved can be updated  */  
   "CanUpdate":boolean,
      /**  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  */  
   "EnableCPQPartCreation":boolean,
   "BitFlag":number,
   "PartNumTypeCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcStrCompRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Part Number of the associated configurator  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  Position order  */  
   "PosOrder":number,
      /**  Name  */  
   "CompName":string,
      /**  Type  */  
   "CompType":string,
      /**  Data Type  */  
   "CompDataType":string,
      /**  Display Format  */  
   "DisplayFormat":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  Defines a starting position for the value of this input in a smart string  */  
   "SmartStringStart":number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   "SmartStringEnd":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  If true then fields on the record may be updated  */  
   "CanUpdate":boolean,
      /**  The coded format to use for a Date component  */  
   "DateFormat":string,
      /**  The separator to use for a date component  */  
   "DateSeparator":string,
      /**  If True a 4 digit year will be used for the date  */  
   "DateFourDigitYear":boolean,
      /**  Use a 3 character month instead of a numeric month  */  
   "DateThreeCharMonth":boolean,
      /**  A coded value indicating the format to use for a logical component  */  
   "LogicalFormat":string,
      /**  The value to use for a True logical value  */  
   "LogicalTrueValue":string,
      /**  The value to use for a False logical value  */  
   "LogicalFalseValue":string,
      /**  The possible values for a Radio-Set, Combo-Box, or validated Character Fill-In  */  
   "PossibleValues":string,
      /**  True if formatting can be applied to the component  */  
   "CanFormat":boolean,
   "SmartStringSeparator":string,
      /**  Number of decimals  */  
   "NumberDecimals":number,
      /**  Number of digits.  */  
   "NumberDigits":number,
      /**  Type of negatives.  */  
   "NumberNegatives":string,
      /**  Thousands' separator.  */  
   "NumberThousands":boolean,
   "BitFlag":number,
   "PartNumIUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackLots":boolean,
   "PartNumPricePerCode":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcTargetEntityRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  TableName  */  
   "TableName":string,
      /**  AllowRecordCreation  */  
   "AllowRecordCreation":boolean,
      /**  AllowPricing  */  
   "AllowPricing":boolean,
      /**  PromptForConfig  */  
   "PromptForConfig":boolean,
      /**  IncomingSmartString  */  
   "IncomingSmartString":boolean,
      /**  Specifies if a configuration that was originally configured in another entity can be reconfigured in the new entity.  */  
   "AllowReconfig":boolean,
      /**  SIValues  */  
   "SIValues":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  If true then detail fields other than Approved can be updated  */  
   "CanUpdate":boolean,
      /**  Description visible of table name  */  
   "TableDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param configID
   */  
export interface BuildCodeEditorInputs_input{
   configID:string,
}

export interface BuildCodeEditorInputs_output{
parameters : {
      /**  output parameters  */  
   availInputs:string,
}
}

   /** Required : 
      @param ds
   */  
export interface BuildSampleSmartString_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface BuildSampleSmartString_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ipConfigID
   */  
export interface ChangingEntConf_input{
      /**  Current Config ID  */  
   ipConfigID:string,
}

export interface ChangingEntConf_output{
parameters : {
      /**  output parameters  */  
   isSynched:boolean,
   settingsExist:boolean,
}
}

   /** Required : 
      @param configID
   */  
export interface CheckConfigAndGetType_input{
      /**  Selected configuration ID  */  
   configID:string,
}

export interface CheckConfigAndGetType_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configType:string,
}
}

   /** Required : 
      @param configID
   */  
export interface CheckForEpicorWebClientSyncUpdates_input{
      /**  ConfigurationID to validate  */  
   configID:string,
}

export interface CheckForEpicorWebClientSyncUpdates_output{
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
   */  
export interface CheckValidRevision_input{
      /**  part number  */  
   ipPartNum:string,
      /**  Revision number  */  
   ipRevisionNum:string,
}

export interface CheckValidRevision_output{
   returnObj:boolean,
}

   /** Required : 
      @param configID
      @param partNum
      @param revisionNum
      @param isInspPlan
   */  
export interface CreatePcStatus_input{
      /**  The configuration ID  */  
   configID:string,
      /**  The configuration part number  */  
   partNum:string,
      /**  The configuration revision number  */  
   revisionNum:string,
      /**  Is this an inspection plan configuration  */  
   isInspPlan:boolean,
}

export interface CreatePcStatus_output{
   returnObj:Erp_Tablesets_ConfiguratorDefTableset[],
}

   /** Required : 
      @param configID
   */  
export interface DeleteByID_input{
   configID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param configID
      @param configPartNum
      @param configRevisionNum
   */  
export interface DeleteConfigSequence_input{
      /**  The configurator ID  */  
   configID:string,
      /**  The configurator part number  */  
   configPartNum:string,
      /**  The configurator revision number  */  
   configRevisionNum:string,
}

export interface DeleteConfigSequence_output{
}

   /** Required : 
      @param configID
      @param isTest
   */  
export interface DeployToEWC_input{
      /**  Configuration ID  */  
   configID:string,
      /**  inidicates whether or not EWC is deploying for the purpose of TestInputs or TestRules  */  
   isTest:boolean,
}

export interface DeployToEWC_output{
   returnObj:Erp_Tablesets_ConfigImportExportTableset[],
}

   /** Required : 
      @param PcDocRulesRowid
      @param ds
   */  
export interface DocRulesMoveDown_input{
      /**  The SysRowID of the rule to be moved down  */  
   PcDocRulesRowid:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface DocRulesMoveDown_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param PcDocRulesRowid
      @param ds
   */  
export interface DocRulesMoveUp_input{
      /**  The SysRowID of the rule to be moved up  */  
   PcDocRulesRowid:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface DocRulesMoveUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param PcDocVarRowid
      @param ds
   */  
export interface DocVarMoveDown_input{
      /**  The RowIdent of the rule to be moved down  */  
   PcDocVarRowid:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface DocVarMoveDown_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param PcDocVarRowid
      @param ds
   */  
export interface DocVarMoveUp_input{
      /**  The RowIdent of the rule to be moved up  */  
   PcDocVarRowid:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface DocVarMoveUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param configID
      @param newConfigID
   */  
export interface DuplicateConfiguration_input{
      /**  The configuration ID to be duplicated.  */  
   configID:string,
      /**  The new configuration ID.  */  
   newConfigID:string,
}

export interface DuplicateConfiguration_output{
}

   /** Required : 
      @param type
      @param configID
      @param ruleSeq
   */  
export interface EditorFilter_input{
      /**  Indicates if will be for session filter or for ColumnFilter  */  
   type:string,
      /**  ConfigID  */  
   configID:string,
      /**  ConfigID  */  
   ruleSeq:number,
}

export interface EditorFilter_output{
   returnObj:string,
}

export interface Erp_Tablesets_CodeEditorPCDatasetTableset{
   CodeEditorPCTargets:Erp_Tablesets_CodeEditorPCTargetsRow[],
   CodeEditorPCDocVars:Erp_Tablesets_CodeEditorPCDocVarsRow[],
   CodeEditorPCInputs:Erp_Tablesets_CodeEditorPCInputsRow[],
   CodeEditorPCMethodVars:Erp_Tablesets_CodeEditorPCMethodVarsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CodeEditorPCDocVarsRow{
   VarName:string,
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCInputsRow{
   InputName:string,
   InputType:string,
   DataType:string,
   PcDynLstCount:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCMethodVarsRow{
   VarName:string,
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CodeEditorPCTargetsRow{
   Company:string,
   TableName:string,
   ColumnName:string,
      /**  Reserved for future development  */  
   ColumnFormat:string,
   ColumnSyntax:string,
      /**  Indicates if the column is from the UD table  */  
   UDColumn:boolean,
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfigImportExportLayeredImageRow{
   Company:string,
   ConfigID:string,
   InputName:string,
   ControlType:string,
   ImageLayerID:string,
   ImageURL:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ConfigImportExportLayeredImageTableset{
   ConfigImportExportLayeredImage:Erp_Tablesets_ConfigImportExportLayeredImageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfigImportExportTableset{
   PcStatus:Erp_Tablesets_PcStatusRow[],
   FileStore:Erp_Tablesets_FileStoreRow[],
   PcAssembly:Erp_Tablesets_PcAssemblyRow[],
   PcAssemblyUsing:Erp_Tablesets_PcAssemblyUsingRow[],
   PcDocRules:Erp_Tablesets_PcDocRulesRow[],
   PcDocRulesExpr:Erp_Tablesets_PcDocRulesExprRow[],
   PcDocVar:Erp_Tablesets_PcDocVarRow[],
   PcDynLst:Erp_Tablesets_PcDynLstRow[],
   PcDynLstCriteria:Erp_Tablesets_PcDynLstCriteriaRow[],
   PcDynLstParams:Erp_Tablesets_PcDynLstParamsRow[],
   PcExpVar:Erp_Tablesets_PcExpVarRow[],
   PcFunctionDef:Erp_Tablesets_PcFunctionDefRow[],
   PcFunctionParam:Erp_Tablesets_PcFunctionParamRow[],
   PcInputs:Erp_Tablesets_PcInputsRow[],
   PcInputsExpr:Erp_Tablesets_PcInputsExprRow[],
   PcInputsLayerDetail:Erp_Tablesets_PcInputsLayerDetailRow[],
   PcInputsLayerHeader:Erp_Tablesets_PcInputsLayerHeaderRow[],
   PcInputsRule:Erp_Tablesets_PcInputsRuleRow[],
   PcInputsRuleDef:Erp_Tablesets_PcInputsRuleDefRow[],
   PcInputVar:Erp_Tablesets_PcInputVarRow[],
   PcMethodVar:Erp_Tablesets_PcMethodVarRow[],
   PcPage:Erp_Tablesets_PcPageRow[],
   PcPageExpr:Erp_Tablesets_PcPageExprRow[],
   PcRules:Erp_Tablesets_PcRulesRow[],
   PcRuleSet:Erp_Tablesets_PcRuleSetRow[],
   PcRulesExpr:Erp_Tablesets_PcRulesExprRow[],
   PcStatusExpr:Erp_Tablesets_PcStatusExprRow[],
   PcStrComp:Erp_Tablesets_PcStrCompRow[],
   PcStruct:Erp_Tablesets_PcStructRow[],
   PcTargetEntity:Erp_Tablesets_PcTargetEntityRow[],
   QBuildMapping:Erp_Tablesets_QBuildMappingRow[],
   QBuildObj:Erp_Tablesets_QBuildObjRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfigurationSequenceTableset{
   PcStruct:Erp_Tablesets_PcStructRow[],
   PcConfigSmartString:Erp_Tablesets_PcConfigSmartStringRow[],
   PcStrComp:Erp_Tablesets_PcStrCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfiguratorDefTableset{
   PcStatus:Erp_Tablesets_PcStatusRow[],
   PcStatusAttch:Erp_Tablesets_PcStatusAttchRow[],
   PcAudit:Erp_Tablesets_PcAuditRow[],
   PcDocRules:Erp_Tablesets_PcDocRulesRow[],
   PcDocRulesExpr:Erp_Tablesets_PcDocRulesExprRow[],
   PcDocVar:Erp_Tablesets_PcDocVarRow[],
   PcInputs:Erp_Tablesets_PcInputsRow[],
   PcStrComp:Erp_Tablesets_PcStrCompRow[],
   PcTargetEntity:Erp_Tablesets_PcTargetEntityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfiguratorDefValueListTableset{
   PcAvailInputsList:Erp_Tablesets_PcAvailInputsListRow[],
   PcPossibleValuesList:Erp_Tablesets_PcPossibleValuesListRow[],
   PcTargetTablesList:Erp_Tablesets_PcTargetTablesListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FileStoreRow{
      /**  SysRowID  */  
   SysRowID:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  RelatedToSchemaName  */  
   RelatedToSchemaName:string,
      /**  RelatedToTable  */  
   RelatedToTable:string,
      /**  Company  */  
   Company:string,
      /**  TenantID  */  
   TenantID:string,
      /**  SecCode  */  
   SecCode:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ModifiedBy  */  
   ModifiedBy:string,
      /**  ModifiedOn  */  
   ModifiedOn:string,
      /**  Content  */  
   Content:string,
      /**  FileName  */  
   FileName:string,
      /**  Category  */  
   Category:string,
      /**  FileType  */  
   FileType:string,
      /**  SysRevID  */  
   SysRevID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KBConfigSearchListRow{
   KBConfigID:number,
   KBConfigDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KBConfigSearchListTableset{
   KBConfigSearchList:Erp_Tablesets_KBConfigSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcAssemblyRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  AssemblyName  */  
   AssemblyName:string,
      /**  Alias  */  
   Alias:string,
      /**  Path  */  
   Path:string,
      /**  IncludeIn  */  
   IncludeIn:number,
      /**  ExternalAssembly  */  
   ExternalAssembly:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Used to determine if the using clauses are to be automatically created when a a new assembly is specified.  */  
   CreateUsingClauses:boolean,
   BitFlag:number,
   PcStatusConfigType:string,
   PcStatusApproved:boolean,
   PcStatusDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcAssemblyUsingRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  AssemblyName  */  
   AssemblyName:string,
      /**  UsingSeq  */  
   UsingSeq:number,
      /**  UsingClause  */  
   UsingClause:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcAuditRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  System Date when this change was made.  */  
   ChgDate:string,
      /**  System Time (seconds since midnight) of when the changes were made.  */  
   ChgTime:number,
      /**  UserID who made the changes.  Not maintainable by the user.  */  
   ChgBy:string,
      /**  Used to enter a description of the changes that were made.  */  
   ChgDescription:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CanUpdate:boolean,
   CvtChgTime:string,
   BitFlag:number,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcAvailInputsListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
   ChoiceDisplay:string,
   ChoiceValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcConfigSmartStringRow{
   Company:string,
   ConfigID:string,
   StringStyle:string,
   PrefacePart:boolean,
      /**  Reserved for future development  */  
   CrtCustPart:boolean,
   Separator:string,
      /**  Reserved for future development  */  
   NumberFormat:string,
   StartNumber:number,
      /**  Reserved for future development  */  
   TargetEntityForSmartString:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDocRulesExprRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Document Rule Sequence Number  */  
   RuleSeq:number,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  Document Rule Expression  */  
   Expression:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ProcessOrder  */  
   ProcessOrder:number,
      /**  ExprType  */  
   ExprType:string,
      /**  LValue  */  
   LValue:string,
      /**  CompareOpr  */  
   CompareOpr:string,
      /**  RValue  */  
   RValue:string,
      /**  RValueType  */  
   RValueType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DispActionString:string,
   dbTable:string,
   dbField:string,
      /**  Assing the default format for the constant editor  */  
   Format:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDocRulesRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  External Company ID  */  
   ExtCompanyID:string,
      /**  Document Rule Sequence Number  */  
   RuleSeq:number,
      /**  Document Rule String  */  
   RuleString:string,
      /**  Document Rule Type  */  
   RuleType:string,
      /**  Name for the calculated field  */  
   CalcName:string,
      /**  Calculated field data type  */  
   CalcDataType:string,
      /**  Database field  */  
   dbField:string,
      /**  Database table  */  
   dbTable:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  Comment  */  
   Comments:string,
      /**  Document Rule Expression  */  
   RuleExpr:string,
      /**  Process Sequence  */  
   ProcessSeq:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  LValue  */  
   LValue:string,
      /**  CompareOpr  */  
   CompareOpr:string,
      /**  RValue  */  
   RValue:string,
      /**  RValueType  */  
   RValueType:string,
      /**  Description  */  
   Description:string,
      /**  ExtCompanyList  */  
   ExtCompanyList:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   dspRuleType:string,
   EntprsConf:boolean,
   TypeCode:string,
   CanUpdate:boolean,
   CompanyName:string,
   dspdbField:string,
   dspdbTable:string,
      /**  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  */  
   MultiCompany:boolean,
      /**  Assing the default format for the constant editor  */  
   Format:string,
   DispLinkString:string,
   BitFlag:number,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDocVarRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  VarNum  */  
   VarNum:number,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  Expression  */  
   Expression:string,
      /**  ExprType  */  
   ExprType:string,
      /**  VarSeq  */  
   VarSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   Format:string,
   CanUpdate:boolean,
   DispLinkString:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDynLstCriteriaRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  The unique sequence id for the dynamic list.  */  
   ListSeq:number,
      /**  Criteria sequence number to make this record unique.  */  
   CriteriaSeq:number,
      /**  Column name to use for BAQ query criteria  */  
   ColumnName:string,
      /**  Condition to use for BAQ query criteria. Options include: =, < >, >, <, >=, <=, BEGINS, MATCHES  */  
   Condition:string,
      /**  This field will indicate where the ColumnValue will be taken from. Current options are BAQ, CONST and INPUT.  */  
   ValueFrom:string,
      /**  This field holds either a constant, a baq column name or a input name from which it will take the value to be used in the BAQ criteria.  */  
   ColumnValue:string,
      /**  Operator to be applied between each criteria. Values are restricted to AND/OR and if none is defined then AND will be used as a default.  */  
   Operator:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  UseEmptyValue  */  
   UseEmptyValue:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Column data type used to identify what type of value should it be compared to, this value should come from the QueryField table.  */  
   ColumnType:string,
      /**  Page Sequence where the parent input exists  */  
   PageSeq:number,
      /**  External field used to temporarily store a display value from which the real value is determined to then be stored in ValueFrom.  */  
   ValueFromDisplay:string,
      /**  BAQ Program Name  */  
   BAQProgramName:string,
   BitFlag:number,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDynLstParamsRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  InputName  */  
   InputName:string,
      /**  ListSeq  */  
   ListSeq:number,
      /**  ParamName  */  
   ParamName:string,
      /**  ParamConst  */  
   ParamConst:boolean,
      /**  ParamValue  */  
   ParamValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Page Sequence where the parent input exists  */  
   PageSeq:number,
      /**  This is the type of Parameter.  */  
   ParamType:string,
   ParamInput:string,
   ParamModifier:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDynLstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Input Name  */  
   InputName:string,
      /**  The unique sequence id for the dynamic list.  */  
   ListSeq:number,
      /**  Contains the logical expression as to when the list is used.  */  
   Condition:string,
      /**  Contains the combo-box list items that are used when the condition is true.  */  
   ListItems:string,
      /**  The Initial value for the list.  */  
   InitVal:string,
      /**  If TRUE then the dynamic list will be built by running a BAQ program  */  
   BAQRunProgram:boolean,
      /**  The BAQ program name used for building the dynamic list  */  
   BAQProgramName:string,
      /**  Value that will be displayed from the BAQ  */  
   BAQDispValue:string,
      /**  The input value for the BAQ  */  
   BAQInputVal:string,
      /**  Defines the type of dynamic list from Static, BAQ, Program, etc.  */  
   ListDataSource:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  RunTblLookup  */  
   RunTblLookup:boolean,
      /**  TblLookupID  */  
   TblLookupID:string,
      /**  TblLookupFunc  */  
   TblLookupFunc:string,
      /**  RunUserDefined  */  
   RunUserDefined:string,
      /**  UserDefinedName  */  
   UserDefinedName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SortOrder  */  
   SortOrder:string,
      /**  SubReturnColumn  */  
   SubReturnColumn:string,
      /**  ScriptCondition  */  
   ScriptCondition:string,
      /**  Reserved for Future Development  */  
   AttributeID:string,
      /**  Identifies if Script expressions are valid for Dynamic List Conditions  */  
   EnableScript:boolean,
   EntprsConf:boolean,
   PageSeq:number,
      /**  Either Client or Server where the UD Method is executed.  */  
   UserDefinedFunctionType:string,
      /**  Storing the Return Type for the selected User Defined Method.  */  
   UserDefinedReturnType:string,
      /**  If true then details on this record can be updated  */  
   CanUpdate:boolean,
   BitFlag:number,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcExpVarRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Tokenized Text used by the expression builder.  */  
   TokenizedText:string,
   CodeEditorText:string,
   AlternateText:string,
   Approved:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcFunctionDefRow{
      /**  Company  */  
   Company:string,
      /**  FunctionName  */  
   FunctionName:string,
      /**  Description  */  
   Description:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  FunctionType  */  
   FunctionType:string,
      /**  Expression  */  
   Expression:string,
      /**  ReturnType  */  
   ReturnType:string,
      /**  OldFunctionName  */  
   OldFunctionName:string,
      /**  IsSync  */  
   IsSync:boolean,
      /**  GlobalFunc  */  
   GlobalFunc:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  BagID  */  
   BagID:string,
      /**  NoInputs  */  
   NoInputs:boolean,
      /**  ScriptExpression  */  
   ScriptExpression:string,
   DispFunctionName:string,
   DispFunctionType:string,
   DispReturnType:string,
      /**  Script expressions are only permitted for PCEMF configurator client expressions.  */  
   BtnEditScript:boolean,
   BitFlag:number,
   PcStatusConfigType:string,
   PcStatusApproved:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcFunctionParamRow{
      /**  Company  */  
   Company:string,
      /**  FunctionName  */  
   FunctionName:string,
      /**  ParameterName  */  
   ParameterName:string,
      /**  DefaultValue  */  
   DefaultValue:string,
      /**  Modifier  */  
   Modifier:string,
      /**  ParamType  */  
   ParamType:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ParamSeq  */  
   ParamSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputVarRow{
      /**  Company  */  
   Company:string,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  InitValue  */  
   InitValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   InitString:string,
   InitDecimal:number,
   InitLogical:boolean,
   InitDate:string,
      /**  Determines if the variable is being used by an input.  */  
   InUse:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  The On Leave expression for the control.  */  
   Expression:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerDetailRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  InputName  */  
   InputName:string,
      /**  ImageLayerID  */  
   ImageLayerID:string,
      /**  LayerSeq  */  
   LayerSeq:number,
      /**  LayerName  */  
   LayerName:string,
      /**  LayerDesc  */  
   LayerDesc:string,
      /**  Order in which layers are placed on the base image.  */  
   ZIndex:number,
      /**  ImageID  */  
   ImageID:string,
      /**  Png type is supported.  */  
   FileType:string,
      /**  Free form text enabling users to categorize layers  */  
   Category:string,
      /**  Width of image  */  
   Width:number,
      /**  Height of image  */  
   Height:number,
      /**  Reserved for Future Development  */  
   xPos:number,
      /**  Reserved for Future Development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerHeaderRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input name this header is assigned.  */  
   InputName:string,
      /**  Image Layer ID.  */  
   ImageLayerID:string,
      /**  File name of the image to be retrieved from the Image URL.  */  
   ImageID:string,
      /**  Description  */  
   Description:string,
      /**  The URL location of the image.  */  
   ImageURL:string,
      /**  File types png and jpg are supported.  */  
   FileType:string,
      /**  Image Width  */  
   Width:number,
      /**  Image height  */  
   Height:number,
      /**  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  */  
   Version:number,
      /**  Reserved for future development  */  
   xPos:number,
      /**  Reserved for future development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  The order that the tab function will step through the inputs.  */  
   TabOrder:number,
      /**  The type of data that can be stored in the control.  */  
   DataType:string,
      /**  The format for which the data will be stored.  */  
   FormatString:string,
      /**  The initial value for the control.  */  
   InitVal:string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   StatusText:string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   Required:boolean,
      /**  On what page does the control exist.  */  
   PageSeq:number,
      /**  The control's label.  */  
   SideLabel:string,
      /**  The pixel position for the x axis.  */  
   xPos:number,
      /**  The pixel position for the Y axis.  */  
   yPos:number,
      /**  The pixel width of the control.  */  
   pWidth:number,
      /**  The pixel height of the control.  */  
   pHeight:number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   ControlType:string,
      /**  The prompt when expression for the widget.  */  
   PromptWhen:string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   ListItems:string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   StartDec:number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   EndDec:number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   IncrPrec:number,
      /**  The starting date for a validated date fill-in.  */  
   StartDate:string,
      /**  The ending date for a validated date fill-in.  */  
   EndDate:string,
      /**  The list of valid responses for a validated string input.  */  
   ValList:string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   Horizontal:boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   IsGlobal:boolean,
      /**  The On Leave expression for the control.  */  
   OnLeave:string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   WebInputName:string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   SummaryLabel:string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   DLRunProgram:boolean,
      /**  The Progress program used for building a dynamic list.  */  
   DLProgramName:string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   DLProgramInputs:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   HideInSummary:boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   OnLeave2:string,
      /**  If true, the input will not be displayed on the input page  */  
   Invisible:boolean,
      /**  Comments describing the input  */  
   Comments:string,
      /**  Global Input Variable  */  
   GlobalInputVar:boolean,
      /**  Global Input Variable Name  */  
   GlbInputVarName:string,
      /**  Do not display input in Summary  */  
   NoDispSummary:boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   ExternalRef:boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   AttributeID:string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMinValue:boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMaxValue:boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseIncrValue:boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseInitVal:boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   UseToolTip:boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseScreenLabel:boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseListValues:boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   SmartPartSeq:number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   SmartStringStart:number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   SmartStringEnd:number,
      /**  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  */  
   ShowDistinct:boolean,
      /**  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  */  
   DesignControlType:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ReadOnly  */  
   ReadOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AutoSizeList  */  
   AutoSizeList:boolean,
      /**  ListWidth  */  
   ListWidth:number,
      /**  ImageSource  */  
   ImageSource:string,
      /**  ImageLayerID  */  
   ImageLayerID:string,
   AllowSmartString:boolean,
   AttributeDescription:string,
      /**  If true then fields on the record may be updated  */  
   CanUpdate:boolean,
   Content:string,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   DispCharVal:string,
   DspPageSeq:number,
      /**  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  */  
   FullInputName:string,
   ImageMapping:boolean,
      /**  The initial value of a date field  */  
   InitDate:string,
      /**  The initial value of a decimal input  */  
   InitDecimal:number,
      /**  The initial value for a logical input  */  
   InitLogical:boolean,
      /**  Indicates whether or not Input Rules have been defined.  */  
   InputRules:boolean,
      /**  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  */  
   InputType:string,
   IsGlobalInputVar:boolean,
   OnLaunch:string,
   PageDisplaySeq:number,
      /**  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  */  
   PcDynLstCount:number,
   ReadOnlyExpression:string,
   TestPlan:boolean,
   ImageURL:string,
   BitFlag:number,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsRuleDefRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  The Input that is updated based upon the rule definition.  */  
   TargetInputName:string,
      /**  Internal column used to keep the rows unique and permit the rule to be resequenced.  */  
   RuleSeq:number,
      /**  The order in which these definitions are interrogated.  */  
   SeqNum:number,
      /**  Input whose value is used in determining if this rule is executed.  */  
   SourceInputName:string,
      /**  Reserved for future development.  Defaults to Value.  */  
   SourceInputProperty:string,
      /**  SourceCharacterValue  */  
   SourceCharacterValue:string,
      /**  SourceIntegerValue  */  
   SourceIntegerValue:number,
      /**  SourceDecimalValue  */  
   SourceDecimalValue:number,
      /**  SourceDateValue  */  
   SourceDateValue:string,
      /**  SourceLogicalValue  */  
   SourceLogicalValue:boolean,
      /**  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  */  
   ProcessSeq:number,
      /**  Reserved for future development.  */  
   LeftP:string,
      /**  Reserved for future development.  */  
   RightP:string,
      /**  Defaults to And and permits users to use more than one input in the rule.  */  
   AndOr:string,
      /**  Comparison operator used when evaluating the rule. Valid value at this time is equals.  */  
   CompOp:string,
      /**  Reserved for future development.  Defaults to false.  */  
   Neg:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   ListValues:string,
   SourceValue:string,
      /**  Input type valid values Label, Character, Numeric, Date, ComboBox  */  
   InputType:string,
   BitFlag:number,
   SourcePcInputsDesignControlType:string,
   SourcePcInputsFormatString:string,
   SourcePcInputsListItems:string,
   SourcePcInputsDataType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsRuleRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  The Input that is updated based upon the rule definition.  */  
   TargetInputName:string,
      /**  Internal column used to keep the rows unique and permit the rule to be resequenced.  */  
   RuleSeq:number,
      /**  Enter text that describes what the rule does.  */  
   RuleDesc:string,
      /**  Reserved for future development.  Defaults to Value.  */  
   TargetInputProperty:string,
      /**  The new value of the input when this rule executes.  */  
   TargetInputValue:string,
      /**  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  */  
   ProcessSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Associated Rule Defintion descriptions  */  
   DefinitionDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcMethodVarRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  AltMethod  */  
   AltMethod:string,
      /**  VarNum  */  
   VarNum:number,
      /**  VarName  */  
   VarName:string,
      /**  DataType  */  
   DataType:string,
      /**  Expression  */  
   Expression:string,
      /**  ExprType  */  
   ExprType:string,
      /**  VarSeq  */  
   VarSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Temporal column to show link phrase  */  
   DispLinkString:string,
   Format:string,
   CanUpdate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcPageExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The configuration page sequence.  */  
   PageSeq:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  The On Leave expression for the control.  */  
   Expression:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcPageRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The configuration page sequence.  */  
   PageSeq:number,
      /**  The title of the configuration page.  */  
   PageTitle:string,
      /**  The prompt when expression for the page.  */  
   PromptWhen:string,
      /**  The On Leave expression for the page  */  
   OnLeave:string,
      /**  If this is set to true then 'On Leave' expressions will not be processed when the input page loads during the configuration process.  Also, if this is set to true then it won't process the 'On Leave' expression for the current input unless the value changes.  If the value changes and the  OnLeave expression for the current input changes the value of another input then it will process the 'On Leave' expression for the other input.  */  
   SkipOnLeaveOPL:boolean,
      /**  Additional field to add OnLeave expressions to the page  */  
   OnLeave2:string,
      /**  Comments  */  
   Comments:string,
      /**  Process dynamic lists before on leave expressions for this page  */  
   ProcessDynLstFirst:boolean,
      /**  Only process dynamic lists with higher tab sequences  */  
   DynLstHigher:boolean,
      /**  Skip processing page on leave on load  */  
   SkipPageProcessOL:boolean,
      /**  Do not process on leave expressions when page loads  */  
   SkipPageNoInputs:boolean,
      /**  Do not process on leave expressions when leaving pages  */  
   SkipOnLeaveOPE:boolean,
      /**  Width of panel  */  
   pWidth:number,
      /**  Height of panel  */  
   pHeight:number,
      /**  Order sequence in which the page will be displayed to the user. This value has been separated from PageSeq.  */  
   DisplaySeq:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ReadOnly  */  
   ReadOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CanUpdate:boolean,
   FirstPage:boolean,
   TestPlan:boolean,
   ReadOnlyExpression:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcPossibleValuesListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
   DisplayValue:string,
   PossibleValue:string,
   SeqNum:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRuleSetRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  PartNum  */  
   PartNum:string,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  AltMethod  */  
   AltMethod:string,
      /**  RuleSetID  */  
   RuleSetID:number,
      /**  BOMElementSysRowID  */  
   BOMElementSysRowID:string,
      /**  BOMElementTableName  */  
   BOMElementTableName:string,
      /**  BOMElementType  */  
   BOMElementType:string,
      /**  RuleTag  */  
   RuleTag:string,
      /**  MtlSeq  */  
   MtlSeq:number,
      /**  OprSeq  */  
   OprSeq:number,
      /**  OpDtlSeq  */  
   OpDtlSeq:number,
      /**  UseKeepWhen  */  
   UseKeepWhen:boolean,
      /**  KeepWhenExpr  */  
   KeepWhenExpr:string,
      /**  KeepWhenLValue  */  
   KeepWhenLValue:string,
      /**  KeepWhenCompareOpr  */  
   KeepWhenCompareOpr:string,
      /**  KeepWhenRValue  */  
   KeepWhenRValue:string,
      /**  KeepWhenRValueType  */  
   KeepWhenRValueType:string,
      /**  KeepWhenType  */  
   KeepWhenType:string,
      /**  ExtCompanyList  */  
   ExtCompanyList:string,
      /**  Comments  */  
   Comments:string,
      /**  Expression  */  
   Expression:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Indicates if is allowed Enterprise Configuration  */  
   EntprsConf:boolean,
   KeepWhenField:string,
   KeepWhenTable:string,
      /**  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  */  
   MultiCompany:boolean,
   AsmPartNum:string,
      /**  If is Enterprise configuration allowed it will update if is Local Company or MultiCompany  */  
   CompanyName:string,
   CanUpdate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  The sequence the rule is going to be applied.  */  
   RuleSeq:number,
      /**  Operation Sequence Number  */  
   OprSeq:number,
      /**  Material Sequence Number  */  
   MtlSeq:number,
      /**  Stores the parent part number within the multi-level BOM for which the rule is related.  */  
   ParPartNum:string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   AsmPartNum:string,
      /**  Alternate Routing method to be used for this rule.  */  
   AltMethod:string,
      /**  Uniquely identifies an OpDtl  */  
   OpDtlSeq:number,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  Method Rule Expression  */  
   Expression:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ProcessOrder  */  
   ProcessOrder:number,
      /**  RuleSetID  */  
   RuleSetID:number,
      /**  ExprType  */  
   ExprType:string,
      /**  LValue  */  
   LValue:string,
      /**  CompareOpr  */  
   CompareOpr:string,
      /**  RValue  */  
   RValue:string,
      /**  RValueType  */  
   RValueType:string,
      /**  ExprXMLItem  */  
   ExprXMLItem:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DispActionString:string,
   BOMElementSysRowID:string,
   BOMElementTableName:string,
   RuleTag:string,
      /**  Assing the default format for the constant editor  */  
   Format:string,
   dbField:string,
   dbTable:string,
   CanUpdate:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcRulesRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  The sequence the rule is going to be applied.  */  
   RuleSeq:number,
      /**  Method Rule String  */  
   RuleString:string,
      /**  Method Rule Type  */  
   RuleType:string,
      /**  Method Rule Expression  */  
   RuleExpr:string,
      /**  Name for the calculated field  */  
   CalcName:string,
      /**  Calculated field data type  */  
   CalcDataType:string,
      /**  Database Field  */  
   dbField:string,
      /**  Database Table  */  
   dbTable:string,
      /**  Operation Sequence Number  */  
   OprSeq:number,
      /**  Material Sequence Number  */  
   MtlSeq:number,
      /**  Stores the parent part number within the multi-level BOM for which the rule is related.  */  
   ParPartNum:string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   AsmPartNum:string,
      /**  Defines what the rule is related to.  Valid values include Par, Opr, Mtl, Asm.  This is used in Gencode.p when creating the compiled code.  */  
   ElementType:string,
      /**  Alternate Routing method to be used for this rule.  */  
   AltMethod:string,
      /**  A unique identifier for the rule.  This will be generated in the database trigger.  */  
   RuleID:number,
      /**  Uniquely identifies an OpDtl  */  
   OpDtlSeq:number,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  Comments  */  
   Comments:string,
      /**  Rule Tag  */  
   RuleTag:string,
      /**  Process Sequence  */  
   ProcessSeq:number,
      /**  LValue  */  
   LValue:string,
      /**  CompareOpr  */  
   CompareOpr:string,
      /**  RValue  */  
   RValue:string,
      /**  RValueType  */  
   RValueType:string,
      /**  RuleSetID  */  
   RuleSetID:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CanUpdate:boolean,
      /**  The node that is currently selected in the tree.  */  
   CurrentNode:string,
   CurrentRuleLineage:string,
      /**  The parent node of the current node that is selected in the tree  */  
   ParentNode:string,
   BOMElementTableName:string,
   BOMElementSysRowID:string,
      /**  Assing the default format for the constant editor  */  
   Format:string,
      /**  Temporal column to show link phrase  */  
   DispLinkString:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStatusAttchRow{
   Company:string,
   ConfigID:string,
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

export interface Erp_Tablesets_PcStatusExprRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  TypeCode  */  
   TypeCode:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  Expression  */  
   Expression:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStatusListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number.  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Configurator Approval Status  */  
   Approved:boolean,
      /**  Date the configuration was approved.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Smart String Style  */  
   StringStyle:string,
      /**  Smart String Seperator character  */  
   Separator:string,
      /**  Smart String Digit Structure  */  
   NumberFormat:string,
      /**  Smart String Starting Sequence  */  
   StartNumber:number,
      /**  Part Creation Method  */  
   CrtCustPart:boolean,
      /**  Smart String preface with part numbner  */  
   PrefacePart:boolean,
      /**  Configurator Version  */  
   ConfigVersion:number,
      /**  Quote Price Code  */  
   QuotePCode:string,
      /**  Order Price Code  */  
   OrderPCode:string,
      /**  OrdQuoCom  */  
   OrdQuoCom:boolean,
      /**  JobPickCom  */  
   JobPickCom:boolean,
      /**  ShipCom  */  
   ShipCom:boolean,
      /**  InvCom  */  
   InvCom:boolean,
      /**  Create Part Flag  */  
   CreatePart:boolean,
      /**  Create part method  */  
   CrtPartUsing:string,
      /**  Create New Part In Quote Entry  */  
   InQuoting:boolean,
      /**  Automatically create a new part number  */  
   AutoCrtPart:boolean,
      /**  Do not prompt user if part exists  */  
   NotUnique:boolean,
      /**  Create New Part In Sales Order Entry  */  
   InOrderEntry:boolean,
      /**  Create New Part In Job Entry  */  
   InJobEntry:boolean,
      /**  Create Bill of Material  */  
   CreateBOM:boolean,
      /**  Create Part at zero cost  */  
   ZeroCost:boolean,
      /**  Create Smart String in part description  */  
   CrtPartDesc:boolean,
      /**  File Name  */  
   FileName:string,
      /**  Added to provide backward compatibility to previous releases.  */  
   SingleLevelConf:boolean,
      /**  Indicates if the input values should be saved.  */  
   SaveInputValues:boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   SetPartNumOnly:boolean,
      /**  Comments  */  
   Comments:string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   AprvRev:boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   EntprsConf:boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   Synchronize:boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   DispConfSummary:boolean,
      /**  Part creation comments  */  
   PartComments:string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   CompPricing:boolean,
      /**  External configurator  */  
   ExtConfig:boolean,
      /**  External company ID  */  
   ExtMfgCompID:string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   TestPlan:boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   MarkMtlGlb:boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   SIValuesUseQt:boolean,
      /**  This field will enable smart string processing for this configuration  */  
   AllowSmartString:boolean,
   InDemandEntry:boolean,
      /**  Demand Price Code  */  
   DemandPCode:string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   AllAltMethods:boolean,
      /**  SIValuesUseGenMethod  */  
   SIValuesUseGenMethod:boolean,
      /**  Description  */  
   Description:string,
      /**  ConfigType  */  
   ConfigType:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ShrinkFieldProperties  */  
   ShrinkFieldProperties:boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   AuditDesc:string,
      /**  A sample smart string constructed from the smart string options  */  
   SampleSmartString:string,
      /**  The available inputs available for use in the smart string  */  
   AvailSmartStringInputs:string,
      /**  The inputs that have been selected for use in the smart string  */  
   SelectedSmartStringInputs:string,
      /**  True if the PartRev record is approved  */  
   RevApproved:boolean,
      /**  If true then detail fields other than Approved can be updated  */  
   CanUpdate:boolean,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   ECOGroup:string,
   IsValidPwd:boolean,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStatusListTableset{
   PcStatusList:Erp_Tablesets_PcStatusListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcStatusRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number.  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Configurator Approval Status  */  
   Approved:boolean,
      /**  Date the configuration was approved.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Smart String Style  */  
   StringStyle:string,
      /**  Smart String Seperator character  */  
   Separator:string,
      /**  Smart String Digit Structure  */  
   NumberFormat:string,
      /**  Smart String Starting Sequence  */  
   StartNumber:number,
      /**  Part Creation Method  */  
   CrtCustPart:boolean,
      /**  Smart String preface with part numbner  */  
   PrefacePart:boolean,
      /**  Configurator Version  */  
   ConfigVersion:number,
      /**  Quote Price Code  */  
   QuotePCode:string,
      /**  Order Price Code  */  
   OrderPCode:string,
      /**  OrdQuoCom  */  
   OrdQuoCom:boolean,
      /**  JobPickCom  */  
   JobPickCom:boolean,
      /**  ShipCom  */  
   ShipCom:boolean,
      /**  InvCom  */  
   InvCom:boolean,
      /**  Create Part Flag  */  
   CreatePart:boolean,
      /**  Create part method  */  
   CrtPartUsing:string,
      /**  Create New Part In Quote Entry  */  
   InQuoting:boolean,
      /**  Automatically create a new part number  */  
   AutoCrtPart:boolean,
      /**  Do not prompt user if part exists  */  
   NotUnique:boolean,
      /**  Create New Part In Sales Order Entry  */  
   InOrderEntry:boolean,
      /**  Create New Part In Job Entry  */  
   InJobEntry:boolean,
      /**  Create Bill of Material  */  
   CreateBOM:boolean,
      /**  Create Part at zero cost  */  
   ZeroCost:boolean,
      /**  Create Smart String in part description  */  
   CrtPartDesc:boolean,
      /**  File Name  */  
   FileName:string,
      /**  Added to provide backward compatibility to previous releases.  */  
   SingleLevelConf:boolean,
      /**  Indicates if the input values should be saved.  */  
   SaveInputValues:boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   SetPartNumOnly:boolean,
      /**  Comments  */  
   Comments:string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   AprvRev:boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   EntprsConf:boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   Synchronize:boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   DispConfSummary:boolean,
      /**  Part creation comments  */  
   PartComments:string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   CompPricing:boolean,
      /**  External configurator  */  
   ExtConfig:boolean,
      /**  External company ID  */  
   ExtMfgCompID:string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   TestPlan:boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   MarkMtlGlb:boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   SIValuesUseQt:boolean,
      /**  This field will enable smart string processing for this configuration  */  
   AllowSmartString:boolean,
   InDemandEntry:boolean,
      /**  Demand Price Code  */  
   DemandPCode:string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   AllAltMethods:boolean,
      /**  AllowReconPO  */  
   AllowReconPO:boolean,
      /**  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  */  
   CompPricingJobMethod:boolean,
      /**  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  */  
   CreateRev:boolean,
      /**  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  */  
   DefaultECO:string,
      /**  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  */  
   GenerateMethod:boolean,
      /**  PromptForConfig  */  
   PromptForConfig:boolean,
      /**  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  */  
   PromptForCheckout:boolean,
      /**  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  */  
   RemoveLink:boolean,
      /**  SIValuesUseGenMethod  */  
   SIValuesUseGenMethod:boolean,
      /**  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  */  
   UseSavedLayout:boolean,
      /**  Description  */  
   Description:string,
      /**  ConfigType  */  
   ConfigType:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  RegenConfig  */  
   RegenConfig:boolean,
      /**  CreateNewConfigID  */  
   CreateNewConfigID:boolean,
      /**  UseTemplatePartDefaults  */  
   UseTemplatePartDefaults:boolean,
      /**  DefaultPartNum  */  
   DefaultPartNum:string,
      /**  DefaultRevisionNum  */  
   DefaultRevisionNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  */  
   AttrClassID:string,
      /**  RecycleJobs  */  
   RecycleJobs:boolean,
      /**  ClientDeployedToEWCDate  */  
   ClientDeployedToEWCDate:string,
      /**  EWCClientSyncRequired  */  
   EWCClientSyncRequired:boolean,
      /**  ShrinkFieldProperties  */  
   ShrinkFieldProperties:boolean,
      /**  Kinetic  */  
   Kinetic:boolean,
      /**  KBConfigID  */  
   KBConfigID:number,
      /**  KBConfigDesc  */  
   KBConfigDesc:string,
      /**  The available inputs available for use in the smart string  */  
   AvailSmartStringInputs:string,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   ECOGroup:string,
      /**  Indicates if the configurator has inputs in its design.  */  
   HasInputs:boolean,
   IsValidPwd:boolean,
      /**  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  */  
   ResetPCInputsAttributes:boolean,
      /**  True if the PartRev record is approved  */  
   RevApproved:boolean,
      /**  A sample smart string constructed from the smart string options  */  
   SampleSmartString:string,
      /**  The inputs that have been selected for use in the smart string  */  
   SelectedSmartStringInputs:string,
      /**  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  */  
   UpdateCreatePartTarget:boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   AuditDesc:string,
      /**  If true then detail fields other than Approved can be updated  */  
   CanUpdate:boolean,
      /**  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  */  
   EnableCPQPartCreation:boolean,
   BitFlag:number,
   PartNumTypeCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStrCompRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Part Number of the associated configurator  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Position order  */  
   PosOrder:number,
      /**  Name  */  
   CompName:string,
      /**  Type  */  
   CompType:string,
      /**  Data Type  */  
   CompDataType:string,
      /**  Display Format  */  
   DisplayFormat:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  Defines a starting position for the value of this input in a smart string  */  
   SmartStringStart:number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   SmartStringEnd:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If true then fields on the record may be updated  */  
   CanUpdate:boolean,
      /**  The coded format to use for a Date component  */  
   DateFormat:string,
      /**  The separator to use for a date component  */  
   DateSeparator:string,
      /**  If True a 4 digit year will be used for the date  */  
   DateFourDigitYear:boolean,
      /**  Use a 3 character month instead of a numeric month  */  
   DateThreeCharMonth:boolean,
      /**  A coded value indicating the format to use for a logical component  */  
   LogicalFormat:string,
      /**  The value to use for a True logical value  */  
   LogicalTrueValue:string,
      /**  The value to use for a False logical value  */  
   LogicalFalseValue:string,
      /**  The possible values for a Radio-Set, Combo-Box, or validated Character Fill-In  */  
   PossibleValues:string,
      /**  True if formatting can be applied to the component  */  
   CanFormat:boolean,
   SmartStringSeparator:string,
      /**  Number of decimals  */  
   NumberDecimals:number,
      /**  Number of digits.  */  
   NumberDigits:number,
      /**  Type of negatives.  */  
   NumberNegatives:string,
      /**  Thousands' separator.  */  
   NumberThousands:boolean,
   BitFlag:number,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStructRow{
      /**  Company ID  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Part Number of the parent configured part number  */  
   PartNum:string,
      /**  Revision Number of the parent configured part number  */  
   RevisionNum:string,
      /**  An optional label to identify the purpose of the sub configurator rule.  */  
   ConfLabel:string,
      /**  Sub assembly configured part number that can be run from this configurator based on the condition of this rule  */  
   SubPartNum:string,
      /**  The revision number of the configurator that can be run from this configurator based on the condition of this rule  */  
   SubRevisionNum:string,
      /**  Optional field.  The sales companies do not have the manufacturing information available but the manufacturing company must put the result of the sub configurator somewhere in the method.  The field has 3 options, E (Equal), G (Greater Than), L (Less Than).  The result of this rule will be inserted in the BOM in the location specified in this field.  If no value is entered, the result will be appended at the end of the BOM structure.  */  
   MtlSeq:number,
      /**  Comments describing the structure rule  */  
   Comments:string,
      /**  Default operation sequence  */  
   OprSeq:number,
      /**  Rule Tag  */  
   RuleTag:string,
      /**  Stores the assembly part number within the multi-level BOM for which the rule is related.  */  
   AsmPartNum:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  StructID  */  
   StructID:number,
      /**  RelatedTo  */  
   RelatedTo:string,
      /**  RelatedToID  */  
   RelatedToID:string,
      /**  DisplaySeq  */  
   DisplaySeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  E9PcInValueRuleTag  */  
   E9PcInValueRuleTag:string,
   BasePartNum:string,
   BaseRevisionNum:string,
   CanUpdate:boolean,
   ConfigSysRowID:string,
   ConfigType:string,
   ConfigVersion:number,
   CreatePart:boolean,
   DefaultECO:string,
   DisplayTag:string,
   KeepIt:boolean,
   NewPartNum:string,
   OverwriteSIValues:boolean,
   ParentNewAsm:string,
   PromptForAutoCreate:boolean,
   PromptForCheckout:boolean,
   PromptForPart:boolean,
   PromptForSIValues:boolean,
   ResponseAutoCreatePart:boolean,
   RevExists:boolean,
      /**  Revolving Sequence  */  
   RevolvingSeq:number,
   SavedGroupSeq:number,
   SaveHeadNum:number,
   SIGroupSeq:number,
   SIHeadNum:number,
   SmartString:string,
      /**  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRe the PartRev.SysRowID and SourceTableName will have "PartRev", otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  */  
   SourceSysRowID:string,
      /**  Calculated source table name, if the RelatedTo is "Part" then this column will contain "PartRev" and SourceSysRowID will contain the PartRev.SysRowID, otherwise both columns will be blank. For non PC configurators the source row is the same across parent and child configurators.  */  
   SourceTableName:string,
   StructTag:string,
   SubBasePartNum:string,
   SubBaseRevisionNum:string,
   SubConfigID:string,
   UseKeepWhen:boolean,
   ParentStructID:number,
   GenerateMethod:boolean,
   BitFlag:number,
   PartSellingFactor:number,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartPartDescription:string,
   PartSalesUM:string,
   PartTrackLots:boolean,
   PartIUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcTargetEntityListTableset{
   PcTargetEntity:Erp_Tablesets_PcTargetEntityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcTargetEntityRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  TableName  */  
   TableName:string,
      /**  AllowRecordCreation  */  
   AllowRecordCreation:boolean,
      /**  AllowPricing  */  
   AllowPricing:boolean,
      /**  PromptForConfig  */  
   PromptForConfig:boolean,
      /**  IncomingSmartString  */  
   IncomingSmartString:boolean,
      /**  Specifies if a configuration that was originally configured in another entity can be reconfigured in the new entity.  */  
   AllowReconfig:boolean,
      /**  SIValues  */  
   SIValues:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  If true then detail fields other than Approved can be updated  */  
   CanUpdate:boolean,
      /**  Description visible of table name  */  
   TableDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcTargetTablesListRow{
      /**  Company Identifier  */  
   Company:string,
      /**  ConfigType  */  
   ConfigType:string,
   Code:string,
   Description:string,
   Hide:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QBuildMappingRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  This is the object name.  */  
   ObjName:string,
      /**  This is the name of the object parameter.  */  
   ObjParameter:string,
      /**  Name of the input mapped to this object parameter.  */  
   MappedInputName:string,
      /**  This is the data type of the object parameter.  */  
   ObjParameterDataType:string,
      /**  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  */  
   ObjParameterInitValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DataType:string,
   PageSeq:number,
   BitFlag:number,
   QBuildObjObjType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QBuildObjRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  This is the name of the object.  */  
   ObjName:string,
      /**  This is the object type.  */  
   ObjType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   PageSeq:number,
   DataType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtConfiguratorDefTableset{
   PcStatus:Erp_Tablesets_PcStatusRow[],
   PcStatusAttch:Erp_Tablesets_PcStatusAttchRow[],
   PcAudit:Erp_Tablesets_PcAuditRow[],
   PcDocRules:Erp_Tablesets_PcDocRulesRow[],
   PcDocRulesExpr:Erp_Tablesets_PcDocRulesExprRow[],
   PcDocVar:Erp_Tablesets_PcDocVarRow[],
   PcInputs:Erp_Tablesets_PcInputsRow[],
   PcStrComp:Erp_Tablesets_PcStrCompRow[],
   PcTargetEntity:Erp_Tablesets_PcTargetEntityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param configID
      @param path
      @param fileName
      @param doInputs
      @param doComments
      @param doSequence
      @param doPartCreation
      @param doSmartString
      @param doDocRules
      @param doPcRules
      @param doGlbVar
      @param configImportExportLayeredImageTS
   */  
export interface ExportConfiguration_input{
   configID:string,
   path:string,
   fileName:string,
   doInputs:boolean,
   doComments:boolean,
   doSequence:boolean,
   doPartCreation:boolean,
   doSmartString:boolean,
   doDocRules:boolean,
   doPcRules:boolean,
   doGlbVar:boolean,
   configImportExportLayeredImageTS:Erp_Tablesets_ConfigImportExportLayeredImageTableset[],
}

export interface ExportConfiguration_output{
parameters : {
      /**  output parameters  */  
   configImportExportLayeredImageTS:Erp_Tablesets_ConfigImportExportLayeredImageTableset[],
}
}

   /** Required : 
      @param configID
   */  
export interface GenerateConfigSequence_input{
      /**  The configurator id  */  
   configID:string,
}

export interface GenerateConfigSequence_output{
}

   /** Required : 
      @param configID
   */  
export interface GetAvailDocVariables_input{
      /**  The configuration ID  */  
   configID:string,
}

export interface GetAvailDocVariables_output{
parameters : {
      /**  output parameters  */  
   availDocVars:string,
}
}

   /** Required : 
      @param configID
   */  
export interface GetAvailInputs_input{
   configID:string,
}

export interface GetAvailInputs_output{
   returnObj:Erp_Tablesets_ConfiguratorDefValueListTableset[],
}

   /** Required : 
      @param configID
   */  
export interface GetByID_input{
   configID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConfiguratorDefTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConfiguratorDefTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConfiguratorDefTableset[],
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
      @param configID
      @param udTargetTables
   */  
export interface GetCodeEditorOptions_input{
   configID:string,
   udTargetTables:string,
}

export interface GetCodeEditorOptions_output{
   returnObj:Erp_Tablesets_CodeEditorPCDatasetTableset[],
}

   /** Required : 
      @param optionType
   */  
export interface GetConfigurationOptions_input{
      /**  The type of option to get.
            Valid values are: PartCreateMethods, SmartStringStyles, SeparatorChars, NumberFormats, PriceMultipliers,
            SmartStringDateFormats, SmartStringDateSeparators, SmartStringLogicalFormats, NumFormatSignOptions, HTMLProducts  */  
   optionType:string,
}

export interface GetConfigurationOptions_output{
parameters : {
      /**  output parameters  */  
   optionList:string,
}
}

   /** Required : 
      @param ipConfigID
      @param ipPartNum
   */  
export interface GetEffectiveRevision_input{
      /**  Configuration ID  */  
   ipConfigID:string,
      /**  Configuration ID  */  
   ipPartNum:string,
}

export interface GetEffectiveRevision_output{
   returnObj:string,
}

   /** Required : 
      @param company
      @param configID
      @param compName
   */  
export interface GetFormatString_input{
      /**  The company ID  */  
   company:string,
      /**  The configuration ID  */  
   configID:string,
      /**  The input's name  */  
   compName:string,
}

export interface GetFormatString_output{
parameters : {
      /**  output parameters  */  
   formatString:string,
}
}

   /** Required : 
      @param configID
      @param inputName
   */  
export interface GetInputPossibleValues_input{
      /**  Configurator ID  */  
   configID:string,
      /**  Input name  */  
   inputName:string,
}

export interface GetInputPossibleValues_output{
   returnObj:Erp_Tablesets_ConfiguratorDefValueListTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetKBConfigSearchList_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetKBConfigSearchList_output{
   returnObj:Erp_Tablesets_KBConfigSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipConfigID
   */  
export interface GetLinkedParts_input{
      /**  Configuration ID  */  
   ipConfigID:string,
}

export interface GetLinkedParts_output{
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
   returnObj:Erp_Tablesets_PcStatusListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param revisionNum
      @param chgDate
   */  
export interface GetNewPcAudit_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   partNum:string,
   revisionNum:string,
   chgDate:string,
}

export interface GetNewPcAudit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param ruleSeq
      @param typeCode
   */  
export interface GetNewPcDocRulesExpr_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
   ruleSeq:number,
   typeCode:string,
}

export interface GetNewPcDocRulesExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcDocRules_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
}

export interface GetNewPcDocRules_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcDocVar_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
}

export interface GetNewPcDocVar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcInputs_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
}

export interface GetNewPcInputs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcStatusAttch_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
}

export interface GetNewPcStatusAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPcStatus_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface GetNewPcStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param posOrder
   */  
export interface GetNewPcStrComp_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
   posOrder:number,
}

export interface GetNewPcStrComp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcTargetEntity_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
   configID:string,
}

export interface GetNewPcTargetEntity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param whereClause
   */  
export interface GetPcTargetEntityListIncludeUD_input{
      /**  Search clause  */  
   whereClause:string,
}

export interface GetPcTargetEntityListIncludeUD_output{
   returnObj:Erp_Tablesets_PcTargetEntityListTableset[],
}

   /** Required : 
      @param whereClause
   */  
export interface GetPcTargetEntityList_input{
      /**  Search clause  */  
   whereClause:string,
}

export interface GetPcTargetEntityList_output{
   returnObj:Erp_Tablesets_PcTargetEntityListTableset[],
}

   /** Required : 
      @param ipPartNum
      @param ipConfigID
   */  
export interface GetRevisions_input{
      /**  Selected part number  */  
   ipPartNum:string,
      /**  Current configuration ID  */  
   ipConfigID:string,
}

export interface GetRevisions_output{
   returnObj:string,
}

   /** Required : 
      @param whereClausePcStatus
      @param whereClausePcStatusAttch
      @param whereClausePcAudit
      @param whereClausePcDocRules
      @param whereClausePcDocRulesExpr
      @param whereClausePcDocVar
      @param whereClausePcInputs
      @param whereClausePcStrComp
      @param whereClausePcTargetEntity
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcStatus:string,
   whereClausePcStatusAttch:string,
   whereClausePcAudit:string,
   whereClausePcDocRules:string,
   whereClausePcDocRulesExpr:string,
   whereClausePcDocVar:string,
   whereClausePcInputs:string,
   whereClausePcStrComp:string,
   whereClausePcTargetEntity:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConfiguratorDefTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipCompanyID
      @param ipConfigID
      @param ipPartNum
      @param ipRevisionNum
   */  
export interface GetSequenceForTree_input{
      /**  The company ID to return data for.  */  
   ipCompanyID:string,
      /**  The configuration ID to return data for.  */  
   ipConfigID:string,
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
}

export interface GetSequenceForTree_output{
   returnObj:Erp_Tablesets_ConfigurationSequenceTableset[],
}

   /** Required : 
      @param ipSpecID
   */  
export interface GetSpecRevs_input{
      /**  Specification ID  */  
   ipSpecID:string,
}

export interface GetSpecRevs_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
   */  
export interface GetTargetEntityColumns_input{
   whereClause:string,
}

export interface GetTargetEntityColumns_output{
   returnObj:Erp_Tablesets_CodeEditorPCDatasetTableset[],
}

   /** Required : 
      @param configType
   */  
export interface GetTargetTables_input{
      /**  The config type  */  
   configType:string,
}

export interface GetTargetTables_output{
   returnObj:Erp_Tablesets_ConfiguratorDefValueListTableset[],
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
      @param configID
      @param fileToImport
      @param replComp
      @param aprvConfig
      @param doInputs
      @param doPartCreation
      @param doSmartString
      @param doComments
      @param doSequence
      @param doDocRules
      @param doPcRules
      @param doGlbVar
      @param schemaName
      @param tableName
   */  
export interface ImportConfiguration_input{
      /**  Configuration ID  */  
   configID:string,
      /**  File To Import  */  
   fileToImport:string,
      /**  Replicate Company  */  
   replComp:boolean,
      /**  Approve Configuration on import  */  
   aprvConfig:boolean,
      /**  Include Inputs  */  
   doInputs:string,
      /**  Include Part Creation  */  
   doPartCreation:boolean,
      /**  Include Smart Strings  */  
   doSmartString:boolean,
      /**  Include Comments  */  
   doComments:boolean,
      /**  Include Sequence  */  
   doSequence:string,
      /**  Include Document Rules  */  
   doDocRules:string,
      /**  Include Method Rules  */  
   doPcRules:string,
      /**  Include Input Variables  */  
   doGlbVar:string,
      /**  Schema Name  */  
   schemaName:string,
      /**  Table Name  */  
   tableName:string,
}

export interface ImportConfiguration_output{
parameters : {
      /**  output parameters  */  
   infoMessages:string,
}
}

   /** Required : 
      @param ipConfigID
      @param schemaName
      @param tableName
      @param ipAttrClassID
   */  
export interface OnChangeAttrClassID_input{
      /**  Configuration ID  */  
   ipConfigID:string,
      /**  Part Attribute Class Schema Name  */  
   schemaName:string,
      /**  Part Attribute Class Table Name  */  
   tableName:string,
      /**  Part Attribute Class ID  */  
   ipAttrClassID:string,
}

export interface OnChangeAttrClassID_output{
parameters : {
      /**  output parameters  */  
   opExistAttributes:boolean,
   opDynAttributeConfigWarning:string,
}
}

   /** Required : 
      @param proposedConfigType
      @param ds
   */  
export interface OnChangeConfigType_input{
   proposedConfigType:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangeConfigType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param newValue
      @param ds
   */  
export interface OnChangePcDocRulesExprLValue_input{
      /**  New value for LValue column  */  
   newValue:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangePcDocRulesExprLValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param newValue
      @param ds
   */  
export interface OnChangePcDocRulesLValue_input{
      /**  New value for LValue column  */  
   newValue:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangePcDocRulesLValue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param kbConfigID
      @param ds
   */  
export interface OnChangePcStatusKBConfigID_input{
      /**  CPQ Configurator ID  */  
   kbConfigID:number,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangePcStatusKBConfigID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param multiCompany
      @param ds
   */  
export interface OnChangedDocRuleCompany_input{
      /**  Indicate if is multi company  */  
   multiCompany:boolean,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedDocRuleCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param columnName
      @param whereClause
   */  
export interface OnChangedEntityColumn_input{
   columnName:string,
   whereClause:string,
}

export interface OnChangedEntityColumn_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPcDocRulesExprExprType_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedPcDocRulesExprExprType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPcDocRulesRuleType_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedPcDocRulesRuleType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param newDataType
      @param ds
   */  
export interface OnChangedPcDocVarDataType_input{
      /**  New DataType  */  
   newDataType:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedPcDocVarDataType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangedPcDocVarExprType_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedPcDocVarExprType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param createPart
      @param ds
   */  
export interface OnChangedPcStatusCreatePart_input{
   createPart:boolean,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedPcStatusCreatePart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param NonConfigurable
      @param ds
   */  
export interface OnChangedPcStatusRemoveLink_input{
   NonConfigurable:boolean,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangedPcStatusRemoveLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param newDataType
      @param ds
   */  
export interface OnChangingPcDocVarDataType_input{
   newDataType:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangingPcDocVarDataType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param newVarName
      @param ds
   */  
export interface OnChangingPcDocVarVarName_input{
      /**  New DataType  */  
   newVarName:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface OnChangingPcDocVarVarName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param configID
   */  
export interface PostDeployMessageToEWC_input{
      /**  Configuration ID EWC needs to deploy  */  
   configID:string,
}

export interface PostDeployMessageToEWC_output{
parameters : {
      /**  output parameters  */  
   resultMessage:string,
}
}

   /** Required : 
      @param ipTestPlan
      @param ipConfigID
   */  
export interface PromptForPassword_input{
      /**  Is this a test plan.  */  
   ipTestPlan:boolean,
      /**  Configuration ID of the revisions being synched.  */  
   ipConfigID:string,
}

export interface PromptForPassword_output{
parameters : {
      /**  output parameters  */  
   opPromptForPassword:boolean,
   opRevisionStatus:boolean,
   opRevisionFound:boolean,
}
}

   /** Required : 
      @param ipCompanyID
      @param ipConfigID
      @param ipPartNum
      @param ipRevisionNum
      @param ipManualRefresh
      @param refreshPcValueHead
   */  
export interface RefreshConfiguratorSequence_input{
      /**  The Configuration ID to return data for.  */  
   ipCompanyID:string,
      /**  The Configuration ID to return data for.  */  
   ipConfigID:string,
      /**  The Part number ID to return data for.  */  
   ipPartNum:string,
      /**  The revision number to return data for.  */  
   ipRevisionNum:string,
      /**  True if manually called from within the designer.  */  
   ipManualRefresh:boolean,
      /**  True if the sequence of PcValueHead should be updated.  */  
   refreshPcValueHead:boolean,
}

export interface RefreshConfiguratorSequence_output{
}

   /** Required : 
      @param ds
   */  
export interface RefreshPcStatusBeforeDisapprove_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface RefreshPcStatusBeforeDisapprove_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ipCompanyID
      @param ipConfigID
      @param ipPartNum
      @param ipRevisionNum
      @param ipManualRefresh
   */  
export interface RefreshSubConf_input{
      /**  The Configuration ID to return data for.  */  
   ipCompanyID:string,
      /**  The Configuration ID to return data for.  */  
   ipConfigID:string,
      /**  The Part number ID to return data for.  */  
   ipPartNum:string,
      /**  The revision number to return data for.  */  
   ipRevisionNum:string,
      /**  True if manually called from within the designer.  */  
   ipManualRefresh:boolean,
}

export interface RefreshSubConf_output{
}

   /** Required : 
      @param configID
      @param configImportExportLayeredImageTableset
   */  
export interface RetrievePcLayeredImagesForExport_input{
      /**  configuration ID  */  
   configID:string,
   configImportExportLayeredImageTableset:Erp_Tablesets_ConfigImportExportLayeredImageTableset[],
}

export interface RetrievePcLayeredImagesForExport_output{
parameters : {
      /**  output parameters  */  
   configImportExportLayeredImageTableset:Erp_Tablesets_ConfigImportExportLayeredImageTableset[],
}
}

   /** Required : 
      @param PcPartNum
   */  
export interface SalesKitConfiguration_input{
      /**  The current part number  */  
   PcPartNum:string,
}

export interface SalesKitConfiguration_output{
parameters : {
      /**  output parameters  */  
   SalesKit:boolean,
}
}

   /** Required : 
      @param PcStrCompRowid
      @param ds
   */  
export interface SmartStringMoveDown_input{
      /**  The RowIdent of the input to be moved down  */  
   PcStrCompRowid:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface SmartStringMoveDown_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param PcStrCompRowid
      @param ds
   */  
export interface SmartStringMoveUp_input{
      /**  The RowIdent of the PcStrComp to be moved up  */  
   PcStrCompRowid:string,
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface SmartStringMoveUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ipTestPlan
      @param ipApproved
      @param ipValidPassword
      @param ipConfigID
      @param ipAuditDesc
   */  
export interface SyncRevision_input{
      /**  Is this a test plan configuration  */  
   ipTestPlan:boolean,
      /**  The proposed approval flag  */  
   ipApproved:boolean,
      /**  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method
            in the UserFile BO.  */  
   ipValidPassword:boolean,
      /**  The configurator ID of the revisions to synchronize  */  
   ipConfigID:string,
      /**  The audit description entered for the configuration approval  */  
   ipAuditDesc:string,
}

export interface SyncRevision_output{
parameters : {
      /**  output parameters  */  
   revSynched:boolean,
}
}

   /** Required : 
      @param configID
   */  
export interface TestInputsPostDeployMessageToEWC_input{
   configID:string,
}

export interface TestInputsPostDeployMessageToEWC_output{
parameters : {
      /**  output parameters  */  
   resultMessage:string,
   configRuntimeURL:string,
   testFileName:string,
}
}

   /** Required : 
      @param configID
   */  
export interface UpdateEpicorWebDeployStatus_input{
      /**  Configuration to update the DeployedToEWCDate with the current date time.  */  
   configID:string,
}

export interface UpdateEpicorWebDeployStatus_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConfiguratorDefTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConfiguratorDefTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param PcStructRowID
      @param newDisplaySeq
   */  
export interface UpdatePcStruct_input{
      /**  The RowIdent of the sequence to be moved down  */  
   PcStructRowID:string,
      /**  The new display sequence to assign to the field  */  
   newDisplaySeq:number,
}

export interface UpdatePcStruct_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ValidatePcDocRulesDelete_input{
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}

export interface ValidatePcDocRulesDelete_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfiguratorDefTableset[],
}
}

