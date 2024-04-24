import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PWLocHisSearchSvc
// Description: Part Locations Wip Search Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/$metadata", {
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
   Description: Get PWLocHisSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PWLocHisSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PWLocHisRow
   */  
export function get_PWLocHisSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PWLocHisSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PWLocHisSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PWLocHisSearch item
   Description: Calls GetByID to retrieve the PWLocHisSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PWLocHisSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DateTimeControl Desc: DateTimeControl   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
   */  
export function get_PWLocHisSearches_Company_Plant_JobNum_PartNum_DateTimeControl_AssemblySeq_OprSeq_MtlSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_PCID_AttributeSetID(Company:string, Plant:string, JobNum:string, PartNum:string, DateTimeControl:string, AssemblySeq:string, OprSeq:string, MtlSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, PCID:string, AttributeSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PWLocHisRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches(" + Company + "," + Plant + "," + JobNum + "," + PartNum + "," + DateTimeControl + "," + AssemblySeq + "," + OprSeq + "," + MtlSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + PCID + "," + AttributeSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PWLocHisRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PWLocHisSearch for the service
   Description: Calls UpdateExt to update PWLocHisSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PWLocHisSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DateTimeControl Desc: DateTimeControl   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PWLocHisRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PWLocHisSearches_Company_Plant_JobNum_PartNum_DateTimeControl_AssemblySeq_OprSeq_MtlSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_PCID_AttributeSetID(Company:string, Plant:string, JobNum:string, PartNum:string, DateTimeControl:string, AssemblySeq:string, OprSeq:string, MtlSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, PCID:string, AttributeSetID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches(" + Company + "," + Plant + "," + JobNum + "," + PartNum + "," + DateTimeControl + "," + AssemblySeq + "," + OprSeq + "," + MtlSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + PCID + "," + AttributeSetID + ")", {
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
   Summary: Call UpdateExt to delete PWLocHisSearch item
   Description: Call UpdateExt to delete PWLocHisSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PWLocHisSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param DateTimeControl Desc: DateTimeControl   Required: True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param OprSeq Desc: OprSeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param WareHouseCode Desc: WareHouseCode   Required: True   Allow empty value : True
      @param BinNum Desc: BinNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DimCode Desc: DimCode   Required: True   Allow empty value : True
      @param TrackType Desc: TrackType   Required: True   Allow empty value : True
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PWLocHisSearches_Company_Plant_JobNum_PartNum_DateTimeControl_AssemblySeq_OprSeq_MtlSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_PCID_AttributeSetID(Company:string, Plant:string, JobNum:string, PartNum:string, DateTimeControl:string, AssemblySeq:string, OprSeq:string, MtlSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, PCID:string, AttributeSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/PWLocHisSearches(" + Company + "," + Plant + "," + JobNum + "," + PartNum + "," + DateTimeControl + "," + AssemblySeq + "," + OprSeq + "," + MtlSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + PCID + "," + AttributeSetID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PWLocHisListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePWLocHis:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePWLocHis!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePWLocHis=" + whereClausePWLocHis
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, jobNum:string, partNum:string, dateTimeControl:string, assemblySeq:string, oprSeq:string, mtlSeq:string, wareHouseCode:string, binNum:string, lotNum:string, dimCode:string, trackType:string, pcID:string, attributeSetID:string, epicorHeaders?:Headers){
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
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof dateTimeControl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dateTimeControl=" + dateTimeControl
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
   if(typeof mtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mtlSeq=" + mtlSeq
   }
   if(typeof wareHouseCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "wareHouseCode=" + wareHouseCode
   }
   if(typeof binNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "binNum=" + binNum
   }
   if(typeof lotNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lotNum=" + lotNum
   }
   if(typeof dimCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dimCode=" + dimCode
   }
   if(typeof trackType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "trackType=" + trackType
   }
   if(typeof pcID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcID=" + pcID
   }
   if(typeof attributeSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attributeSetID=" + attributeSetID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetJobInspectionsData
   Description: Retrieves Part Locations Inspections related to a Job
   OperationID: GetJobInspectionsData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobInspectionsData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobInspectionsData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJobInspectionsData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetJobInspectionsData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartInspectionsData
   Description: Retrieves Part Locations Inspections related to a Part
   OperationID: GetPartInspectionsData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInspectionsData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInspectionsData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartInspectionsData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetPartInspectionsData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPWLocHis
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPWLocHis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPWLocHis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPWLocHis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPWLocHis(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetNewPWLocHis", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PWLocHisSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PWLocHisListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PWLocHisRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PWLocHisRow[],
}

export interface Erp_Tablesets_PWLocHisListRow{
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
      /**  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  */  
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
      /**  Unit of Measure of items in the container.  */  
   "UM":string,
      /**  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  */  
   "FinalOp":boolean,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  User ID that created the record.  */  
   "CreatedBy":string,
      /**  Date that record was created.  */  
   "CreatedDate":string,
      /**  System time record was created.(secounds from midnight).  */  
   "CreatedTime":number,
      /**   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  */  
   "DateTimeControl":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description for the TrackType column  */  
   "TrackTypeDescription":string,
   "DispCreatedTime":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PWLocHisRow{
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
      /**  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  */  
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
      /**  Unit of Measure of items in the container.  */  
   "UM":string,
      /**  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  */  
   "FinalOp":boolean,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  User ID that created the record.  */  
   "CreatedBy":string,
      /**  Date that record was created.  */  
   "CreatedDate":string,
      /**  System time record was created.(secounds from midnight).  */  
   "CreatedTime":number,
      /**   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  */  
   "DateTimeControl":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Description for the TrackType column  */  
   "TrackTypeDescription":string,
   "DispCreatedTime":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
   "BitFlag":number,
   "OpMasterOpDesc":string,
   "ResourceGroupDescription":string,
   "WarehouseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param plant
      @param jobNum
      @param partNum
      @param dateTimeControl
      @param assemblySeq
      @param oprSeq
      @param mtlSeq
      @param wareHouseCode
      @param binNum
      @param lotNum
      @param dimCode
      @param trackType
      @param pcID
      @param attributeSetID
   */  
export interface DeleteByID_input{
   plant:string,
   jobNum:string,
   partNum:string,
   dateTimeControl:number,
   assemblySeq:number,
   oprSeq:number,
   mtlSeq:number,
   wareHouseCode:string,
   binNum:string,
   lotNum:string,
   dimCode:string,
   trackType:string,
   pcID:string,
   attributeSetID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PWInspectDSTableset{
   PWInspect:Erp_Tablesets_PWInspectRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PWInspectRow{
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  */  
   AssemblySeq:number,
      /**  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  */  
   BinNum:string,
      /**  Job number.  Unique key to identify the production job  */  
   JobNum:string,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  */  
   JobSeq:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  A unique part number that identifies the part that comes from the RcvDtl or NonConf table record.  */  
   PartNum:string,
      /**  The PO line # which is being received. Only applicable for PO receipt transactions.  */  
   POLine:number,
      /**  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  */  
   PONum:number,
      /**  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exis  */  
   PurPoint:string,
      /**  Transaction Quantity  */  
   Quantity:number,
      /**  Description of the Inspection record which depends on the table that the information comes from. If the record comes from the RcvDtl table this type is set to "Receipt", if it comes from the NonConf this type is set to "Assemblies", "Inventory", "Materials" depending on the NonConf.TrnTyp field being "D", "I" or "M" respectively.  */  
   RecordType:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   Revision:string,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   RMALine:number,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   RMANum:number,
      /**  Denotes the JobSeqType and is set to "MTL" if the JobSeqType or the TrnTyp of the RcvDtl or NonConf record respectively equals "M", or it is set to "SUB" when it equals "S".  */  
   SeqType:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorID:string,
      /**  Unique identifier for the warehouse that comes from the RcvDtl or NonConf table.  */  
   WarehouseCode:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustID:string,
      /**  Vendor's or Customer's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   Name:string,
      /**  Plant  */  
   Plant:string,
      /**  TranID of related NonConf record.  */  
   NonConfTranID:number,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Warehouse Description.  */  
   WarehouseDescription:string,
      /**  Unit of Measure.  */  
   IUM:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of Pieces  */  
   DispNumberOfPieces:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PWLocHisListRow{
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
      /**  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  */  
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
      /**  Unit of Measure of items in the container.  */  
   UM:string,
      /**  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  */  
   FinalOp:boolean,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  User ID that created the record.  */  
   CreatedBy:string,
      /**  Date that record was created.  */  
   CreatedDate:string,
      /**  System time record was created.(secounds from midnight).  */  
   CreatedTime:number,
      /**   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  */  
   DateTimeControl:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description for the TrackType column  */  
   TrackTypeDescription:string,
   DispCreatedTime:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PWLocHisListTableset{
   PWLocHisList:Erp_Tablesets_PWLocHisListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PWLocHisRow{
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
      /**  Job operation sequence number that part is allocated to. Note: As quantity is reported against an operation, it is allocated to the "Next" operation sequence.  */  
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
      /**  Unit of Measure of items in the container.  */  
   UM:string,
      /**  Indicates if the completed (OutPut) quantity is for the final operation.  It is used as a filter in Part Tracker to find completed quantities that have not been moved off the job.  */  
   FinalOp:boolean,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  User ID that created the record.  */  
   CreatedBy:string,
      /**  Date that record was created.  */  
   CreatedDate:string,
      /**  System time record was created.(secounds from midnight).  */  
   CreatedTime:number,
      /**   An integer which represents date and time the record was created expressed in minutes from the MfgSys base date which is 10/30/1953. This field is used as a component of the primary index to insure uniqueness and provide an index in date/time sequence.
Calculated as: ((TODAY - 11/30/1953) * 1440) + (TIME / 60).  */  
   DateTimeControl:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Description for the TrackType column  */  
   TrackTypeDescription:string,
   DispCreatedTime:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   BitFlag:number,
   OpMasterOpDesc:string,
   ResourceGroupDescription:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PWLocHisSearchTableset{
   PWLocHis:Erp_Tablesets_PWLocHisRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPWLocHisSearchTableset{
   PWLocHis:Erp_Tablesets_PWLocHisRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param jobNum
      @param partNum
      @param dateTimeControl
      @param assemblySeq
      @param oprSeq
      @param mtlSeq
      @param wareHouseCode
      @param binNum
      @param lotNum
      @param dimCode
      @param trackType
      @param pcID
      @param attributeSetID
   */  
export interface GetByID_input{
   plant:string,
   jobNum:string,
   partNum:string,
   dateTimeControl:number,
   assemblySeq:number,
   oprSeq:number,
   mtlSeq:number,
   wareHouseCode:string,
   binNum:string,
   lotNum:string,
   dimCode:string,
   trackType:string,
   pcID:string,
   attributeSetID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PWLocHisSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PWLocHisSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PWLocHisSearchTableset[],
}

   /** Required : 
      @param jobNum
   */  
export interface GetJobInspectionsData_input{
      /**  Job Number  */  
   jobNum:string,
}

export interface GetJobInspectionsData_output{
   returnObj:Erp_Tablesets_PWInspectDSTableset[],
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
   returnObj:Erp_Tablesets_PWLocHisListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param jobNum
      @param partNum
      @param dateTimeControl
      @param assemblySeq
      @param oprSeq
      @param mtlSeq
      @param wareHouseCode
      @param binNum
      @param lotNum
      @param dimCode
      @param trackType
      @param pcID
   */  
export interface GetNewPWLocHis_input{
   ds:Erp_Tablesets_PWLocHisSearchTableset[],
   plant:string,
   jobNum:string,
   partNum:string,
   dateTimeControl:number,
   assemblySeq:number,
   oprSeq:number,
   mtlSeq:number,
   wareHouseCode:string,
   binNum:string,
   lotNum:string,
   dimCode:string,
   trackType:string,
   pcID:string,
}

export interface GetNewPWLocHis_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PWLocHisSearchTableset[],
}
}

   /** Required : 
      @param partNum
   */  
export interface GetPartInspectionsData_input{
      /**  Job Number  */  
   partNum:string,
}

export interface GetPartInspectionsData_output{
   returnObj:Erp_Tablesets_PWInspectDSTableset[],
}

   /** Required : 
      @param whereClausePWLocHis
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePWLocHis:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PWLocHisSearchTableset[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPWLocHisSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPWLocHisSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PWLocHisSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PWLocHisSearchTableset[],
}
}

