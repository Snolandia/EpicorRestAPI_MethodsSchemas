import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartWipSearchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/$metadata", {
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
   Description: Get PartWipSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartWipSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipRow
   */  
export function get_PartWipSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartWipSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartWipRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartWipRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartWipSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartWipSearch item
   Description: Calls GetByID to retrieve the PartWipSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWipSearch
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
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartWipRow
   */  
export function get_PartWipSearches_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_PCID_AttributeSetID_SysRowID(Company:string, Plant:string, PartNum:string, JobNum:string, AssemblySeq:string, OprSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, PCID:string, AttributeSetID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartWipRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + PCID + "," + AttributeSetID + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartWipRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartWipSearch for the service
   Description: Calls UpdateExt to update PartWipSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartWipSearch
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
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartWipRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartWipSearches_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_PCID_AttributeSetID_SysRowID(Company:string, Plant:string, PartNum:string, JobNum:string, AssemblySeq:string, OprSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, PCID:string, AttributeSetID:string, SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + PCID + "," + AttributeSetID + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PartWipSearch item
   Description: Call UpdateExt to delete PartWipSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartWipSearch
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
      @param PCID Desc: PCID   Required: True   Allow empty value : True
      @param AttributeSetID Desc: AttributeSetID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartWipSearches_Company_Plant_PartNum_JobNum_AssemblySeq_OprSeq_WareHouseCode_BinNum_LotNum_DimCode_TrackType_MtlSeq_PCID_AttributeSetID_SysRowID(Company:string, Plant:string, PartNum:string, JobNum:string, AssemblySeq:string, OprSeq:string, WareHouseCode:string, BinNum:string, LotNum:string, DimCode:string, TrackType:string, MtlSeq:string, PCID:string, AttributeSetID:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/PartWipSearches(" + Company + "," + Plant + "," + PartNum + "," + JobNum + "," + AssemblySeq + "," + OprSeq + "," + WareHouseCode + "," + BinNum + "," + LotNum + "," + DimCode + "," + TrackType + "," + MtlSeq + "," + PCID + "," + AttributeSetID + "," + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWipListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipListRow)
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
export function get_GetRows(whereClausePartWip:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartWip!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartWip=" + whereClausePartWip
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, partNum:string, jobNum:string, assemblySeq:string, oprSeq:string, wareHouseCode:string, binNum:string, lotNum:string, dimCode:string, trackType:string, mtlSeq:string, pcID:string, attributeSetID:string, sysRowID:string, epicorHeaders?:Headers){
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
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
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
   if(typeof mtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mtlSeq=" + mtlSeq
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
   if(typeof sysRowID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysRowID=" + sysRowID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetPartWipOprList
   OperationID: GetPartWipOprList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartWipOprList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartWipOprList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartWipOprList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetPartWipOprList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsJobTracker
   Description: Returns PartWip records for Job Tracker
   OperationID: Get_GetRowsJobTracker
      @param jobNum Desc: Job Number   Required: True   Allow empty value : True
      @param trackType Desc: Track type records to return   Required: True   Allow empty value : True
      @param wipCompleteOnly Desc: Return only completed for Wip   Required: True
      @param excludePartLocations Desc: Exclude part locations   Required: True
      @param pageSize Desc: Page Size   Required: True
      @param absolutePage Desc: Absolute Page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsJobTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRowsJobTracker(jobNum:string, trackType:string, wipCompleteOnly:string, excludePartLocations:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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
   if(typeof trackType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "trackType=" + trackType
   }
   if(typeof wipCompleteOnly!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "wipCompleteOnly=" + wipCompleteOnly
   }
   if(typeof excludePartLocations!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "excludePartLocations=" + excludePartLocations
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetRowsJobTracker" + params, {
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
   Summary: Invoke method GetNewPartWip
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartWip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartWip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartWip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartWip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetNewPartWip", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartWipSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartWipListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWipRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartWipRow[],
}

export interface Erp_Tablesets_PartWipListRow{
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  ResourceGroup Output Warehouse  */  
   "OutputWhse":string,
      /**  Output BinNum from ResourceGroup  */  
   "OutputBinNum":string,
      /**  Operation Description  */  
   "OpDesc":string,
      /**  Resource Group Description  */  
   "ResGrpDescription":string,
      /**  Tells if the current row is the first occurence for the operation or not.  */  
   "IsDistinct":boolean,
      /**  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   "TranQty":number,
      /**  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   "TranUOM":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "JobPartDescription":string,
      /**  Describes the Part.  */  
   "PartPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartTrackLots":boolean,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  Description.  */  
   "WarehouseDescription":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartWipRow{
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Package Control Identification Number  */  
   "PCID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  */  
   "LaborEntryMethod":string,
      /**  Operation Description  */  
   "OpDesc":string,
      /**  Output BinNum from ResourceGroup  */  
   "OutputBinNum":string,
      /**  ResourceGroup Output Warehouse  */  
   "OutputWhse":string,
      /**  Resource Group Description  */  
   "ResGrpDescription":string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   "SubContract":boolean,
      /**  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   "TranQty":number,
      /**  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   "TranUOM":string,
      /**  Tells if the current row is the first occurence for the operation or not.  */  
   "IsDistinct":boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "DispNumberOfPieces":number,
   "BitFlag":number,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobPartDescription":string,
   "PartTrackLots":boolean,
   "PartSalesUM":string,
   "PartPricePerCode":string,
   "PartIUM":string,
   "PartSellingFactor":number,
   "PartTrackDimension":boolean,
   "PartPartDescription":string,
   "PartTrackSerialNum":boolean,
   "PlantName":string,
   "WarehouseDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
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
      @param pcID
      @param attributeSetID
      @param sysRowID
   */  
export interface DeleteByID_input{
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
   pcID:string,
   attributeSetID:number,
   sysRowID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartWipListRow{
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  ResourceGroup Output Warehouse  */  
   OutputWhse:string,
      /**  Output BinNum from ResourceGroup  */  
   OutputBinNum:string,
      /**  Operation Description  */  
   OpDesc:string,
      /**  Resource Group Description  */  
   ResGrpDescription:string,
      /**  Tells if the current row is the first occurence for the operation or not.  */  
   IsDistinct:boolean,
      /**  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   TranQty:number,
      /**  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   TranUOM:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   JobPartDescription:string,
      /**  Describes the Part.  */  
   PartPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartTrackLots:boolean,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  Description.  */  
   WarehouseDescription:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartWipListTableset{
   PartWipList:Erp_Tablesets_PartWipListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartWipRow{
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time and Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  Operation Description  */  
   OpDesc:string,
      /**  Output BinNum from ResourceGroup  */  
   OutputBinNum:string,
      /**  ResourceGroup Output Warehouse  */  
   OutputWhse:string,
      /**  Resource Group Description  */  
   ResGrpDescription:string,
      /**  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  */  
   SubContract:boolean,
      /**  Quantity converted to the TranUOM, which can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   TranQty:number,
      /**  Can be the same as UM if the Part tracks multiple UOM and if not it will be the Part.IUM.  */  
   TranUOM:string,
      /**  Tells if the current row is the first occurence for the operation or not.  */  
   IsDistinct:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobPartDescription:string,
   PartTrackLots:boolean,
   PartSalesUM:string,
   PartPricePerCode:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartTrackDimension:boolean,
   PartPartDescription:string,
   PartTrackSerialNum:boolean,
   PlantName:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartWipSearchTableset{
   PartWip:Erp_Tablesets_PartWipRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartWipSearchTableset{
   PartWip:Erp_Tablesets_PartWipRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
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
      @param pcID
      @param attributeSetID
      @param sysRowID
   */  
export interface GetByID_input{
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
   pcID:string,
   attributeSetID:number,
   sysRowID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartWipSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartWipSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartWipSearchTableset[],
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
   returnObj:Erp_Tablesets_PartWipListTableset[],
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
      @param pcID
      @param attributeSetID
   */  
export interface GetNewPartWip_input{
   ds:Erp_Tablesets_PartWipSearchTableset[],
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
   pcID:string,
   attributeSetID:number,
}

export interface GetNewPartWip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartWipSearchTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetPartWipOprList_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetPartWipOprList_output{
   returnObj:Erp_Tablesets_PartWipListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param jobNum
      @param trackType
      @param wipCompleteOnly
      @param excludePartLocations
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsJobTracker_input{
      /**  Job Number  */  
   jobNum:string,
      /**  Track type records to return  */  
   trackType:string,
      /**  Return only completed for Wip  */  
   wipCompleteOnly:boolean,
      /**  Exclude part locations  */  
   excludePartLocations:boolean,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsJobTracker_output{
   returnObj:Erp_Tablesets_PartWipSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePartWip
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartWip:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartWipSearchTableset[],
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
   ds:Erp_Tablesets_UpdExtPartWipSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartWipSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartWipSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartWipSearchTableset[],
}
}

