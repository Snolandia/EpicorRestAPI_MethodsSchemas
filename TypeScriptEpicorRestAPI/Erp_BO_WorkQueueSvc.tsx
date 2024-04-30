import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.WorkQueueSvc
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get WorkQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WorkQueues
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkQueueRow
   */  
export function get_WorkQueues(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WorkQueues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WorkQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.WorkQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WorkQueues(requestBody:Erp_Tablesets_WorkQueueRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WorkQueue item
   Description: Calls GetByID to retrieve the WorkQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WorkQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.WorkQueueRow
   */  
export function get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WorkQueueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_WorkQueueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WorkQueue for the service
   Description: Calls UpdateExt to update WorkQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WorkQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.WorkQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WorkQueues_Company_JobNum_AssemblySeq_OprSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, requestBody:Erp_Tablesets_WorkQueueRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete WorkQueue item
   Description: Call UpdateExt to delete WorkQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WorkQueue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WorkQueues_Company_JobNum_AssemblySeq_OprSeq(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get LaborOperActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborOperActions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborOperActionRow
   */  
export function get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_LaborOperActions(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborOperActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/LaborOperActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborOperActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborOperAction item
   Description: Calls GetByID to retrieve the LaborOperAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborOperAction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborOperActionRow
   */  
export function get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_LaborOperActions_SysRowID(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborOperActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/LaborOperActions(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborOperActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PartWipOps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartWipOps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipOpRow
   */  
export function get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_PartWipOps(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipOpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/PartWipOps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipOpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartWipOp item
   Description: Calls GetByID to retrieve the PartWipOp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWipOp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartWipOpRow
   */  
export function get_WorkQueues_Company_JobNum_AssemblySeq_OprSeq_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company:string, JobNum:string, AssemblySeq:string, OprSeq:string, Plant:string, PartNum:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, AttributeSetID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartWipOpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/WorkQueues(" + Company + "," + JobNum + "," + AssemblySeq + "," + OprSeq + ")/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartWipOpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get LaborOperActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborOperActions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborOperActionRow
   */  
export function get_LaborOperActions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborOperActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborOperActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborOperActions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.LaborOperActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LaborOperActions(requestBody:Erp_Tablesets_LaborOperActionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the LaborOperAction item
   Description: Calls GetByID to retrieve the LaborOperAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborOperAction
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.LaborOperActionRow
   */  
export function get_LaborOperActions_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborOperActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborOperActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LaborOperAction for the service
   Description: Calls UpdateExt to update LaborOperAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborOperAction
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborOperActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LaborOperActions_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_LaborOperActionRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions(" + SysRowID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete LaborOperAction item
   Description: Call UpdateExt to delete LaborOperAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborOperAction
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LaborOperActions_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/LaborOperActions(" + SysRowID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
   Description: Get PartWipOps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartWipOps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipOpRow
   */  
export function get_PartWipOps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipOpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipOpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartWipOps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartWipOpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartWipOps(requestBody:Erp_Tablesets_PartWipOpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartWipOp item
   Description: Calls GetByID to retrieve the PartWipOp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWipOp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartWipOpRow
   */  
export function get_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company:string, Plant:string, PartNum:string, JobNum:string, AssemblySeq:string, OprSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, AttributeSetID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartWipOpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartWipOpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartWipOp for the service
   Description: Calls UpdateExt to update PartWipOp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartWipOp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartWipOpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company:string, Plant:string, PartNum:string, JobNum:string, AssemblySeq:string, OprSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, AttributeSetID:string, SysRowID:string, requestBody:Erp_Tablesets_PartWipOpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete PartWipOp item
   Description: Call UpdateExt to delete PartWipOp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartWipOp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartWipOps_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_AttributeSetID_SysRowID(Company:string, Plant:string, PartNum:string, JobNum:string, AssemblySeq:string, OprSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, AttributeSetID:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/PartWipOps(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + AttributeSetID + "," + SysRowID + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkQueueListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseWorkQueue:string, whereClauseLaborOperAction:string, whereClausePartWipOp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseWorkQueue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWorkQueue=" + whereClauseWorkQueue
   }
   if(typeof whereClauseLaborOperAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborOperAction=" + whereClauseLaborOperAction
   }
   if(typeof whereClausePartWipOp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartWipOp=" + whereClausePartWipOp
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRows_output)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, assemblySeq:string, oprSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof assemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assemblySeq=" + assemblySeq
   }
   if(typeof oprSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "oprSeq=" + oprSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOpsInResourceGroup
   Description: To build the priority dispatch temp table (JCR65) from the JobOper records for the given workcenter.
This procedure reads the JobOper, and sets values of certain variables used by the BuildTempTable
procedure defined in JCR65-RP.i
   OperationID: GetOpsInResourceGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOpsInResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOpsInResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOpsInResourceGroup(requestBody:GetOpsInResourceGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOpsInResourceGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetOpsInResourceGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetOpsInResourceGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLaborOperActionDS
   Description: GetLaborOperActionDS
   OperationID: GetLaborOperActionDS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLaborOperActionDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLaborOperActionDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLaborOperActionDS(requestBody:GetLaborOperActionDS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLaborOperActionDS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetLaborOperActionDS", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLaborOperActionDS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOpsInResourceGroupWithBaq
   Description: Extension of GetOpsInResourceGroup which takes a BAQ, executes and processes the results for the Work Queue.
   OperationID: Get_GetOpsInResourceGroupWithBaq
      @param ipBaqID Desc: BAQ Query ID   Required: True   Allow empty value : True
      @param ipResourceGrpID Desc: Resource Group ID   Required: True   Allow empty value : True
      @param ipEmpID Desc: Employee ID   Required: True   Allow empty value : True
      @param ipLaborType Desc: Labor Type   Required: True   Allow empty value : True
      @param ipStartDate Desc: Start Date to cut off from   Required: True   Allow empty value : True
      @param ipJobNum Desc: Job, empty will exclude from filter   Required: True   Allow empty value : True
      @param ipAssemblySeq Desc: Assembly Seq, empty will exclude from filter   Required: True   Allow empty value : True
      @param ipOpCode Desc: Operation Code, empty will exclude from filter   Required: True   Allow empty value : True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute Page   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOpsInResourceGroupWithBaq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetOpsInResourceGroupWithBaq(ipBaqID:string, ipResourceGrpID:string, ipEmpID:string, ipLaborType:string, ipStartDate:string, ipJobNum:string, ipAssemblySeq:string, ipOpCode:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ipBaqID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipBaqID=" + ipBaqID
   }
   if(typeof ipResourceGrpID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipResourceGrpID=" + ipResourceGrpID
   }
   if(typeof ipEmpID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipEmpID=" + ipEmpID
   }
   if(typeof ipLaborType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipLaborType=" + ipLaborType
   }
   if(typeof ipStartDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipStartDate=" + ipStartDate
   }
   if(typeof ipJobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipJobNum=" + ipJobNum
   }
   if(typeof ipAssemblySeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipAssemblySeq=" + ipAssemblySeq
   }
   if(typeof ipOpCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ipOpCode=" + ipOpCode
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

   return (new Promise<GetOpsInResourceGroupWithBaq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetOpsInResourceGroupWithBaq" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetOpsInResourceGroupWithBaq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshSelectedRecords
   Description: Refresh the selected records within the Work Queue
   OperationID: RefreshSelectedRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshSelectedRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshSelectedRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshSelectedRecords(requestBody:RefreshSelectedRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshSelectedRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/RefreshSelectedRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RefreshSelectedRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EndActivity
   Description: End Activity on the selected work.
   OperationID: EndActivity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EndActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EndActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EndActivity(requestBody:EndActivity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EndActivity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/EndActivity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as EndActivity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewWorkQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWorkQueue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewWorkQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWorkQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWorkQueue(requestBody:GetNewWorkQueue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewWorkQueue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetNewWorkQueue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewWorkQueue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartWipOp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartWipOp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartWipOp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartWipOp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartWipOp(requestBody:GetNewPartWipOp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartWipOp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetNewPartWipOp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartWipOp_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.WorkQueueSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateExt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborOperActionRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborOperActionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipOpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartWipOpRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WorkQueueListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkQueueRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WorkQueueRow,
}

export interface Erp_Tablesets_LaborOperActionRow{
      /**  Description of Action.  */  
   "ActionDesc":string,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   "ActionSeq":number,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   "AssemblySeq":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if this Action was completed.  */  
   "Completed":boolean,
      /**  The number of the employee that performed the work.  */  
   "CompletedBy":string,
      /**  Name of the user ID in CompletedBy  */  
   "CompletedByName":string,
      /**  Date the Action was completed.  */  
   "CompletedOn":string,
      /**  JobNum  */  
   "JobNum":string,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborDtlSeq":number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   "LaborHedSeq":number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   "OprSeq":number,
      /**  Indicated if this Action must be completed before Operation can be completed.  */  
   "Required":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartWipOpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Part Number of item in the container.  */  
   "PartNum":string,
      /**  Job Number that the part allocated to.  */  
   "JobNum":string,
      /**  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  */  
   "AssemblySeq":number,
      /**  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  */  
   "OprSeq":number,
      /**  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  */  
   "MtlSeq":number,
      /**   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  */  
   "WareHouseCode":string,
      /**  Unique lot number for the parts.  */  
   "LotNum":string,
      /**  Unique dimension code for the parts.  */  
   "DimCode":string,
      /**   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  */  
   "BinNum":string,
      /**   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  */  
   "TrackType":string,
      /**  Resource Group of the related operation.  */  
   "ResourceGrpID":string,
      /**  Operation code of the related job operation.  */  
   "OpCode":string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  */  
   "Quantity":number,
      /**  Unit of Measure of items in the container.  */  
   "UM":string,
      /**  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  */  
   "FromAssemblySeq":number,
      /**  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  */  
   "FromOprSeq":number,
      /**  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  */  
   "FromResourceGrpID":string,
      /**  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  */  
   "FromOpCode":string,
      /**  Last Activity Date.  */  
   "LastActivityDate":string,
      /**  Time of last activity expressed in seconds from midnight.  */  
   "LastActivityTime":number,
      /**  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  */  
   "FinalOp":boolean,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  */  
   "UpdateStageQty":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "TrackTypeDesc":string,
   "PartDescription":string,
      /**  Used for caching pagination in UI  */  
   "PageNum":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WorkQueueListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   "JCDept":string,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  The total operation quantity. This is a calculated field.  */  
   "OprQty":number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
   "SetupLoadHrs":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
   "ProdLoadHrs":number,
      /**  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  */  
   "RegionCode":number,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "StartHour":number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   "DueHour":number,
   "SortDate":string,
   "WIPQty":number,
      /**  Number Of Employees Now Working On This Operation  */  
   "CrewCount":number,
   "QtyLeft":number,
   "SetupLeft":number,
      /**  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  */  
   "WIPQtyDetails":boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  TRUE indicates the current employee is authorized to Request Material  */  
   "CanRequest":boolean,
      /**  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  */  
   "CanSelect":boolean,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Part number of the manufactured item.  */  
   "JobHeadPartNum":string,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  The description of the part that is to be manufactured.  */  
   "JobHeadPartDescription":string,
      /**  Editor widget for Job operation comments.  */  
   "OprCommentText":string,
      /**  Editor widget for Job header comments.  */  
   "AsmCommentText":string,
      /**  Editor widget for Job header comments.  */  
   "JobHeadCommentText":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  */  
   "RegionDescription":string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   "OpDtlSeq":number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   "PartNum":string,
      /**  Description is initially created when the JobOpDtl is created.  */  
   "OpDtlDescription":string,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  */  
   "OpDtlType":string,
      /**  Description used only for subcontract operations  */  
   "Description":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "SortHour":number,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**  Used by the UI to allow selection of rows  */  
   "Selected":boolean,
      /**  Description for PartNum  */  
   "PartDescription":string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**  Delimited list of resources oper is schedueld to  */  
   "SchResourceList":string,
      /**  Current Production Qty (for user reporting qty)  */  
   "CurQty":number,
      /**  Qty currently being completed  */  
   "LaborQty":number,
      /**  Scrap Qty currently being entered  */  
   "ScrapQty":number,
      /**  Discrep Qty currently being entered  */  
   "DiscrepQty":number,
      /**  Reason code for discrep qty currently being entered  */  
   "DiscrepRsnCode":string,
      /**  Reason code for scrap currently being entered  */  
   "ScrapRsnCode":string,
      /**  Description for ScrapRsnCode  */  
   "ScrapRsnDesc":string,
      /**  Description for DescrepRsnCode  */  
   "DiscrepRsnDesc":string,
      /**  Operation complete  */  
   "Complete":boolean,
   "ResourceID":string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  CustNum from first order  */  
   "FirstCustNum":number,
   "FirstCustID":string,
   "FirstCustName":string,
   "FirstShipViaCode":string,
   "FirstShipViaDesc":string,
   "SetupGrpDesc":string,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
   "CheckBox05":boolean,
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WorkQueueRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   "JCDept":string,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   "OpComplete":boolean,
      /**  Job Number  */  
   "JobNum":string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   "OprSeq":number,
      /**  The total operation quantity. This is a calculated field.  */  
   "OprQty":number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   "OpCode":string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   "EstSetHours":number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   "EstProdHours":number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   "ProdStandard":number,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
   "SetupLoadHrs":number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
   "ProdLoadHrs":number,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   "OpsPerPart":number,
      /**  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  */  
   "RegionCode":number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "StartHour":number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   "DueHour":number,
   "SortDate":string,
   "WIPQty":number,
      /**  Number Of Employees Now Working On This Operation  */  
   "CrewCount":number,
   "QtyLeft":number,
   "SetupLeft":number,
      /**  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  */  
   "WIPQtyDetails":boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   "Machines":number,
      /**  TRUE indicates the current employee is authorized to Request Material  */  
   "CanRequest":boolean,
      /**  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  */  
   "CanSelect":boolean,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   "SetUpCrewSize":number,
      /**  Part number of the manufactured item.  */  
   "JobHeadPartNum":string,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   "ProdCrewSize":number,
      /**  The description of the part that is to be manufactured.  */  
   "JobHeadPartDescription":string,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   "QtyCompleted":number,
      /**  Editor widget for Job operation comments.  */  
   "OprCommentText":string,
      /**  Editor widget for Job header comments.  */  
   "AsmCommentText":string,
      /**  Editor widget for Job header comments.  */  
   "JobHeadCommentText":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  */  
   "RegionDescription":string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   "OpDtlSeq":number,
      /**  Description is initially created when the JobOpDtl is created.  */  
   "OpDtlDescription":string,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   "PartNum":string,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  */  
   "OpDtlType":string,
      /**  Description used only for subcontract operations  */  
   "Description":string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   "SortHour":number,
      /**  Editor widget for Job operation comments.  */  
   "CommentText":string,
      /**  Used by the UI to allow selection of rows  */  
   "Selected":boolean,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   "RunQty":number,
      /**  Description for PartNum  */  
   "PartDescription":string,
      /**  Delimited list of resources oper is schedueld to  */  
   "SchResourceList":string,
      /**  Current Production Qty (for user reporting qty)  */  
   "CurQty":number,
      /**  Qty currently being completed  */  
   "LaborQty":number,
      /**  Scrap Qty currently being entered  */  
   "ScrapQty":number,
      /**  Discrep Qty currently being entered  */  
   "DiscrepQty":number,
      /**  Reason code for discrep qty currently being entered  */  
   "DiscrepRsnCode":string,
      /**  Reason code for scrap currently being entered  */  
   "ScrapRsnCode":string,
      /**  Description for ScrapRsnCode  */  
   "ScrapRsnDesc":string,
      /**  Description for DescrepRsnCode  */  
   "DiscrepRsnDesc":string,
      /**  Operation complete  */  
   "Complete":boolean,
   "ResourceID":string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  CustNum from first order  */  
   "FirstCustNum":number,
   "FirstCustID":string,
   "FirstCustName":string,
   "FirstShipViaCode":string,
   "FirstShipViaDesc":string,
   "SetupGrpDesc":string,
      /**  Used to group operation to save on setups.  */  
   "SetupGroup":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RequestMove  */  
   "RequestMove":boolean,
   "ResourceGrpID":string,
   "SetupOrProd":string,
      /**  Used to checks if the StartDate has a value or is null to later permit a Sorting of the records By the StartDate field , positioning the null values at the end.  */  
   "StartDateNullCheck":boolean,
   "CheckBox01":boolean,
   "CheckBox02":boolean,
   "CheckBox03":boolean,
   "CheckBox04":boolean,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
   "CheckBox05":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
   "Date01":string,
   "Date02":string,
   "Date03":string,
   "Date04":string,
   "Date05":string,
   "Number01":number,
   "Number02":number,
   "Number03":number,
   "Number04":number,
   "Number05":number,
   "ShortChar01":string,
   "ShortChar02":string,
   "ShortChar03":string,
   "ShortChar04":string,
   "ShortChar05":string,
      /**  Used for caching pagination in UI  */  
   "PageNum":number,
      /**  Used for caching pagination in UI  */  
   "TotalRecords":number,
      /**  Used for caching pagination in UI  */  
   "MorePages":boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) , "B" - Backflush or "X" - Time and Backflush Qty.  */  
   "LaborEntryMethodDesc":string,
   "EnableLaborQty":boolean,
   "EnableScrapQty":boolean,
   "EnableDiscrepQty":boolean,
      /**  Resource Group Description.  */  
   "ResourceGrpDesc":string,
      /**  Operation Code Description.  */  
   "OpCodeOpDesc":string,
      /**  Unit of Measure used for editable quantity fields on the WorkQueue.  */  
   "LaborUOM":string,
   "LaborType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param jobNum
      @param assemblySeq
      @param oprSeq
   */  
export interface DeleteByID_input{
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
      @param ipBaqID
      @param ipResourceGrpID
      @param ipEmpID
   */  
export interface EndActivity_input{
   ds:Erp_Tablesets_WorkQueueTableset[],
      /**  BAQ query ID to execute when returning results  */  
   ipBaqID:string,
      /**  Resource Group ID  */  
   ipResourceGrpID:string,
      /**  Employee ID  */  
   ipEmpID:string,
}

export interface EndActivity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkQueueTableset,
}
}

export interface Erp_Tablesets_LaborOperActionRow{
      /**  Description of Action.  */  
   ActionDesc:string,
      /**  A sequence number which uniquely identifies action record within the operation set.  */  
   ActionSeq:number,
      /**  A sequence number which uniquely identifies the assembly record within the method.  */  
   AssemblySeq:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if this Action was completed.  */  
   Completed:boolean,
      /**  The number of the employee that performed the work.  */  
   CompletedBy:string,
      /**  Name of the user ID in CompletedBy  */  
   CompletedByName:string,
      /**  Date the Action was completed.  */  
   CompletedOn:string,
      /**  JobNum  */  
   JobNum:string,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborDtlSeq:number,
      /**  Used as the foreign key to the LaborDtl record.  */  
   LaborHedSeq:number,
      /**  A sequence number which uniquely identifies the operation record within the method.  */  
   OprSeq:number,
      /**  Indicated if this Action must be completed before Operation can be completed.  */  
   Required:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartWipOpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Part Number of item in the container.  */  
   PartNum:string,
      /**  Job Number that the part allocated to.  */  
   JobNum:string,
      /**  Assembly Sequence that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence which may be on the next assembly sequence.  */  
   AssemblySeq:number,
      /**  job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  */  
   OprSeq:number,
      /**  The MtlSeq of the related JobMtl record.  Pertains only to  Raw Materials (TrackType = "R")  */  
   MtlSeq:number,
      /**   Warehouse Code of the warehouse where the container of parts are currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutWhse of the workcenter that created the parts.  */  
   WareHouseCode:string,
      /**  Unique lot number for the parts.  */  
   LotNum:string,
      /**  Unique dimension code for the parts.  */  
   DimCode:string,
      /**   Warehouse Bin where the container is currently located.
FYI: Reporting of production quantity initially sets this to the WrkCenter.OutPutBinNum of the workcenter that created the parts.  */  
   BinNum:string,
      /**   Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.
"R" - Raw Material a part which was issued to the job.
"M" - Manufactured Part. The part that is being manufactured.  */  
   TrackType:string,
      /**  Resource Group of the related operation.  */  
   ResourceGrpID:string,
      /**  Operation code of the related job operation.  */  
   OpCode:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Part Quantity balance for a  Job/Asm/Opr at a warehouse/bin location.  */  
   Quantity:number,
      /**  Unit of Measure of items in the container.  */  
   UM:string,
      /**  Assembly Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  */  
   FromAssemblySeq:number,
      /**  Operation Sequence # which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  */  
   FromOprSeq:number,
      /**  Resource Group which created the parts allocated to this operation.  This only pertains to semi-finished manufactured parts (TrackType = M)  */  
   FromResourceGrpID:string,
      /**  Operation Code which created the parts allocated to this operation. Note, this only pertains to semi finished manufactured parts (TrackType = M)  */  
   FromOpCode:string,
      /**  Last Activity Date.  */  
   LastActivityDate:string,
      /**  Time of last activity expressed in seconds from midnight.  */  
   LastActivityTime:number,
      /**  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  */  
   FinalOp:boolean,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Used in the PartWip write trigger to control update to JobMtl.QtyStagedToDate field. Only transactions which  move the material in/out of the staging area update this field.  This field will contain the transaction type that moved the material. For example; STK-MTL(issue of stock), PUR-MTL( movement of purchased material), MTL-STK( Returns to stock).  */  
   UpdateStageQty:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   TrackTypeDesc:string,
   PartDescription:string,
      /**  Used for caching pagination in UI  */  
   PageNum:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtWorkQueueTableset{
   WorkQueue:Erp_Tablesets_WorkQueueRow[],
   LaborOperAction:Erp_Tablesets_LaborOperActionRow[],
   PartWipOp:Erp_Tablesets_PartWipOpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WorkQueueListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   JCDept:string,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  The total operation quantity. This is a calculated field.  */  
   OprQty:number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
   SetupLoadHrs:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
   ProdLoadHrs:number,
      /**  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  */  
   RegionCode:number,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
   SortDate:string,
   WIPQty:number,
      /**  Number Of Employees Now Working On This Operation  */  
   CrewCount:number,
   QtyLeft:number,
   SetupLeft:number,
      /**  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  */  
   WIPQtyDetails:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  TRUE indicates the current employee is authorized to Request Material  */  
   CanRequest:boolean,
      /**  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  */  
   CanSelect:boolean,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Part number of the manufactured item.  */  
   JobHeadPartNum:string,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  The description of the part that is to be manufactured.  */  
   JobHeadPartDescription:string,
      /**  Editor widget for Job operation comments.  */  
   OprCommentText:string,
      /**  Editor widget for Job header comments.  */  
   AsmCommentText:string,
      /**  Editor widget for Job header comments.  */  
   JobHeadCommentText:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  */  
   RegionDescription:string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Description is initially created when the JobOpDtl is created.  */  
   OpDtlDescription:string,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  */  
   OpDtlType:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   SortHour:number,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**  Used by the UI to allow selection of rows  */  
   Selected:boolean,
      /**  Description for PartNum  */  
   PartDescription:string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**  Delimited list of resources oper is schedueld to  */  
   SchResourceList:string,
      /**  Current Production Qty (for user reporting qty)  */  
   CurQty:number,
      /**  Qty currently being completed  */  
   LaborQty:number,
      /**  Scrap Qty currently being entered  */  
   ScrapQty:number,
      /**  Discrep Qty currently being entered  */  
   DiscrepQty:number,
      /**  Reason code for discrep qty currently being entered  */  
   DiscrepRsnCode:string,
      /**  Reason code for scrap currently being entered  */  
   ScrapRsnCode:string,
      /**  Description for ScrapRsnCode  */  
   ScrapRsnDesc:string,
      /**  Description for DescrepRsnCode  */  
   DiscrepRsnDesc:string,
      /**  Operation complete  */  
   Complete:boolean,
   ResourceID:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  CustNum from first order  */  
   FirstCustNum:number,
   FirstCustID:string,
   FirstCustName:string,
   FirstShipViaCode:string,
   FirstShipViaDesc:string,
   SetupGrpDesc:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
   CheckBox05:boolean,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WorkQueueListTableset{
   WorkQueueList:Erp_Tablesets_WorkQueueListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WorkQueueRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  */  
   JCDept:string,
      /**   Indicates if this operation is completed. This is normally set to complete via labor entry transactions.   Not maintainable by Job Entry. It can't be reset to "No" if the JobHead.Complete = Yes.
Labor entry setting logic is: If SetUpComplete = Yes and  EstProdHours = 0 or ProdComplete = Yes and EstSetHours = 0 or both ProdComplete = Yes and SetupComplete = Yes  then OpComplete = Yes.
This field is also set by PO receipt entry "issue complete" for subcontract operations.  */  
   OpComplete:boolean,
      /**  Job Number  */  
   JobNum:string,
      /**  Assembly Sequence # that this Operation is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  The total operation quantity. This is a calculated field.  */  
   OprQty:number,
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**  Total estimated set up hours.  Calculated as EstSetHoursPerMch * Machines.  It is set to zero if operation qty is zero.  This is maintained via the JobOper write trigger.  */  
   EstSetHours:number,
      /**   The estimated Production run hours for internal operations (JobOper.Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (JobOper.RunQty / Std).
If StdFormat = "PM" then (JobOper.RunQty / Std ) / 60.
If StdFormat = "OH" then (JobOper.RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((JobOper.RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (JobOPer.RunQty/Basis) X Std.
If StdFormat = "MP" then ((JobOper.RunQty/Basis) X Std) / 60.  */  
   EstProdHours:number,
      /**   The production standard for the operation.  It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours.  A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  */  
   ProdStandard:number,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
   SetupLoadHrs:number,
      /**   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
   ProdLoadHrs:number,
      /**  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  */  
   OpsPerPart:number,
      /**  1=CurrentWork, 2=AvailableWork, 3=ExpectedWork  */  
   RegionCode:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
   SortDate:string,
   WIPQty:number,
      /**  Number Of Employees Now Working On This Operation  */  
   CrewCount:number,
   QtyLeft:number,
   SetupLeft:number,
      /**  TRUE indicates there are WIP Qty Details available (i.e. the Staged Details button should be enabled)  */  
   WIPQtyDetails:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  TRUE indicates the current employee is authorized to Request Material  */  
   CanRequest:boolean,
      /**  TRUE indicates the current employee can select this operation to work on (i.e. the Select For Work button should be enabled).  */  
   CanSelect:boolean,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Part number of the manufactured item.  */  
   JobHeadPartNum:string,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  The description of the part that is to be manufactured.  */  
   JobHeadPartDescription:string,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   QtyCompleted:number,
      /**  Editor widget for Job operation comments.  */  
   OprCommentText:string,
      /**  Editor widget for Job header comments.  */  
   AsmCommentText:string,
      /**  Editor widget for Job header comments.  */  
   JobHeadCommentText:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  "Current Work", "Available Work", or "Expected Work" as indicated by the RegionCode.  */  
   RegionDescription:string,
      /**  Uniquely identifies an OpDtl.  System assigned.  */  
   OpDtlSeq:number,
      /**  Description is initially created when the JobOpDtl is created.  */  
   OpDtlDescription:string,
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "Setup", "Production", or "Both".  */  
   OpDtlType:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   SortHour:number,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**  Used by the UI to allow selection of rows  */  
   Selected:boolean,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**  Description for PartNum  */  
   PartDescription:string,
      /**  Delimited list of resources oper is schedueld to  */  
   SchResourceList:string,
      /**  Current Production Qty (for user reporting qty)  */  
   CurQty:number,
      /**  Qty currently being completed  */  
   LaborQty:number,
      /**  Scrap Qty currently being entered  */  
   ScrapQty:number,
      /**  Discrep Qty currently being entered  */  
   DiscrepQty:number,
      /**  Reason code for discrep qty currently being entered  */  
   DiscrepRsnCode:string,
      /**  Reason code for scrap currently being entered  */  
   ScrapRsnCode:string,
      /**  Description for ScrapRsnCode  */  
   ScrapRsnDesc:string,
      /**  Description for DescrepRsnCode  */  
   DiscrepRsnDesc:string,
      /**  Operation complete  */  
   Complete:boolean,
   ResourceID:string,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  CustNum from first order  */  
   FirstCustNum:number,
   FirstCustID:string,
   FirstCustName:string,
   FirstShipViaCode:string,
   FirstShipViaDesc:string,
   SetupGrpDesc:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RequestMove  */  
   RequestMove:boolean,
   ResourceGrpID:string,
   SetupOrProd:string,
      /**  Used to checks if the StartDate has a value or is null to later permit a Sorting of the records By the StartDate field , positioning the null values at the end.  */  
   StartDateNullCheck:boolean,
   CheckBox01:boolean,
   CheckBox02:boolean,
   CheckBox03:boolean,
   CheckBox04:boolean,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
   CheckBox05:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   Date01:string,
   Date02:string,
   Date03:string,
   Date04:string,
   Date05:string,
   Number01:number,
   Number02:number,
   Number03:number,
   Number04:number,
   Number05:number,
   ShortChar01:string,
   ShortChar02:string,
   ShortChar03:string,
   ShortChar04:string,
   ShortChar05:string,
      /**  Used for caching pagination in UI  */  
   PageNum:number,
      /**  Used for caching pagination in UI  */  
   TotalRecords:number,
      /**  Used for caching pagination in UI  */  
   MorePages:boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) , "B" - Backflush or "X" - Time and Backflush Qty.  */  
   LaborEntryMethodDesc:string,
   EnableLaborQty:boolean,
   EnableScrapQty:boolean,
   EnableDiscrepQty:boolean,
      /**  Resource Group Description.  */  
   ResourceGrpDesc:string,
      /**  Operation Code Description.  */  
   OpCodeOpDesc:string,
      /**  Unit of Measure used for editable quantity fields on the WorkQueue.  */  
   LaborUOM:string,
   LaborType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_WorkQueueTableset{
   WorkQueue:Erp_Tablesets_WorkQueueRow[],
   LaborOperAction:Erp_Tablesets_LaborOperActionRow[],
   PartWipOp:Erp_Tablesets_PartWipOpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
      @param assemblySeq
      @param oprSeq
   */  
export interface GetByID_input{
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_WorkQueueTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_WorkQueueTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_WorkQueueTableset[],
}

   /** Required : 
      @param ds
      @param jobNum
      @param assySeq
      @param oprSeq
      @param empNum
   */  
export interface GetLaborOperActionDS_input{
   ds:Erp_Tablesets_WorkQueueTableset[],
      /**  The employee Code of the current employee.  */  
   jobNum:string,
      /**  The employee Code of the current employee.  */  
   assySeq:number,
      /**  The employee Code of the current employee.  */  
   oprSeq:number,
      /**  The employee Code of the current employee.  */  
   empNum:string,
}

export interface GetLaborOperActionDS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkQueueTableset,
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
   returnObj:Erp_Tablesets_WorkQueueListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param partNum
      @param jobNum
      @param assemblySeq
      @param oprSeq
      @param wareHouseCode
      @param binNum
      @param lotNum
      @param dimCode
      @param trackType
      @param mtlSeq
      @param attributeSetID
   */  
export interface GetNewPartWipOp_input{
   ds:Erp_Tablesets_WorkQueueTableset[],
   plant:string,
   partNum:string,
   jobNum:string,
   assemblySeq:number,
   oprSeq:number,
   wareHouseCode:string,
   binNum:string,
   lotNum:string,
   dimCode:string,
   trackType:string,
   mtlSeq:number,
   attributeSetID:number,
}

export interface GetNewPartWipOp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkQueueTableset,
}
}

   /** Required : 
      @param ds
      @param jobNum
      @param assemblySeq
   */  
export interface GetNewWorkQueue_input{
   ds:Erp_Tablesets_WorkQueueTableset[],
   jobNum:string,
   assemblySeq:number,
}

export interface GetNewWorkQueue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkQueueTableset,
}
}

   /** Required : 
      @param ipBaqID
      @param ipResourceGrpID
      @param ipEmpID
      @param ipLaborType
      @param ipStartDate
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOpCode
      @param pageSize
      @param absolutePage
   */  
export interface GetOpsInResourceGroupWithBaq_input{
      /**  BAQ Query ID  */  
   ipBaqID:string,
      /**  Resource Group ID  */  
   ipResourceGrpID:string,
      /**  Employee ID  */  
   ipEmpID:string,
      /**  Labor Type  */  
   ipLaborType:string,
      /**  Start Date to cut off from  */  
   ipStartDate:string,
      /**  Job, empty will exclude from filter  */  
   ipJobNum:string,
      /**  Assembly Seq, empty will exclude from filter  */  
   ipAssemblySeq:string,
      /**  Operation Code, empty will exclude from filter  */  
   ipOpCode:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetOpsInResourceGroupWithBaq_output{
   returnObj:Erp_Tablesets_WorkQueueTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
   opTotalWorkQueueRecords:number,
}
}

   /** Required : 
      @param pcResourceGrpID
      @param pcEmpID
      @param pageSize
      @param absolutePage
      @param LaborType
      @param clearCache
      @param filterParameters
   */  
export interface GetOpsInResourceGroup_input{
      /**  The Code of the Resource Group for which the operations should be retrieved.  */  
   pcResourceGrpID:string,
      /**  The employee Code of the current employee.  */  
   pcEmpID:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
      /**  Labor Type  */  
   LaborType:string,
      /**  Clear CACHE: true/false  */  
   clearCache:boolean,
      /**  Concatenated string of filters, Start Date in ISO Format YYYYMMDD, Job Number, Assembly Seq and Operation Description. Ex '20151231~2031~0~DEBUR'  */  
   filterParameters:string,
}

export interface GetOpsInResourceGroup_output{
   returnObj:Erp_Tablesets_WorkQueueTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
   totalWorkQueueRecords:number,
}
}

   /** Required : 
      @param whereClauseWorkQueue
      @param whereClauseLaborOperAction
      @param whereClausePartWipOp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseWorkQueue:string,
   whereClauseLaborOperAction:string,
   whereClausePartWipOp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_WorkQueueTableset[],
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
      @param ds
      @param ipBaqID
      @param ipResourceGrpID
      @param ipEmpID
   */  
export interface RefreshSelectedRecords_input{
   ds:Erp_Tablesets_WorkQueueTableset[],
      /**  BAQ query ID to execute when returning results  */  
   ipBaqID:string,
      /**  Resource Group ID  */  
   ipResourceGrpID:string,
      /**  Employee ID  */  
   ipEmpID:string,
}

export interface RefreshSelectedRecords_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkQueueTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtWorkQueueTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtWorkQueueTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_WorkQueueTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_WorkQueueTableset,
}
}

