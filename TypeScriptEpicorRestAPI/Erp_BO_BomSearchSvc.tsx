import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.BomSearchSvc
// Description: bo/BomSearch/BomSearch.p
           To return records from the bom option for drag/drop inside
           Job Entry, QuoteAsm Entry, and Engineering Work Bench and any
           other places that may need to search this data.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", {
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
   Summary: Invoke method CreatePartMtlRefDes
   Description: Create Part Material Reference
   OperationID: CreatePartMtlRefDes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePartMtlRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePartMtlRefDes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreatePartMtlRefDes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/CreatePartMtlRefDes", {
          method: 'post',
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
         resolve(data as CreatePartMtlRefDes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAllAlternateTrees
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartMtlRefDes, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
ALL ALTERNATES OF THE PARTREVISION WILL BE RETURNED if ipcomplete is true
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
   OperationID: GetAllAlternateTrees
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAllAlternateTrees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllAlternateTrees_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllAlternateTrees(requestBody:GetAllAlternateTrees_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAllAlternateTrees_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/GetAllAlternateTrees", {
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
         resolve(data as GetAllAlternateTrees_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
This method will also allow you to return the whole dataset or allow the user to specify how
the revision to return possible "part" records for.
   OperationID: GetDatasetForTree
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTree(requestBody:GetDatasetForTree_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDatasetForTree_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/GetDatasetForTree", {
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
         resolve(data as GetDatasetForTree_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTreeByProcessMfgID
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
This method will also allow you to return the whole dataset or allow the user to specify how
the revision to return possible "part" records for.
   OperationID: GetDatasetForTreeByProcessMfgID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeByProcessMfgID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeByProcessMfgID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTreeByProcessMfgID(requestBody:GetDatasetForTreeByProcessMfgID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDatasetForTreeByProcessMfgID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/GetDatasetForTreeByProcessMfgID", {
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
         resolve(data as GetDatasetForTreeByProcessMfgID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDatasetForTreeWithPartValidation
   Description: Validates Part, finds default revision based on asOfDate and invokes GetDatasetForTree.
   OperationID: GetDatasetForTreeWithPartValidation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeWithPartValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeWithPartValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDatasetForTreeWithPartValidation(requestBody:GetDatasetForTreeWithPartValidation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDatasetForTreeWithPartValidation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/GetDatasetForTreeWithPartValidation", {
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
         resolve(data as GetDatasetForTreeWithPartValidation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartRevExists
   Description: Part Revision Exists
   OperationID: PartRevExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartRevExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartRevExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartRevExists(requestBody:PartRevExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartRevExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/PartRevExists", {
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
         resolve(data as PartRevExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartNumSource
   Description: Gets PartNum of the source record
   OperationID: GetPartNumSource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartNumSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartNumSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartNumSource(requestBody:GetPartNumSource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartNumSource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/GetPartNumSource", {
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
         resolve(data as GetPartNumSource_output)
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
export interface CreatePartMtlRefDes_output{
}

export interface Erp_Tablesets_BomSearchTableset{
   PartRev:Erp_Tablesets_PartRevRow[],
   PartRevAttch:Erp_Tablesets_PartRevAttchRow[],
   PartMtl:Erp_Tablesets_PartMtlRow[],
   PartMtlAttch:Erp_Tablesets_PartMtlAttchRow[],
   PartMtlInsp:Erp_Tablesets_PartMtlInspRow[],
   PartMtlRestriction:Erp_Tablesets_PartMtlRestrictionRow[],
   PartMtlRestrictSubst:Erp_Tablesets_PartMtlRestrictSubstRow[],
   PartOpr:Erp_Tablesets_PartOprRow[],
   PartOprAttch:Erp_Tablesets_PartOprAttchRow[],
   PartOpDtl:Erp_Tablesets_PartOpDtlRow[],
   PartOprInsp:Erp_Tablesets_PartOprInspRow[],
   PartOprRestriction:Erp_Tablesets_PartOprRestrictionRow[],
   PartOprRestrictSubst:Erp_Tablesets_PartOprRestrictSubstRow[],
   PartOprAction:Erp_Tablesets_PartOprActionRow[],
   PartOprActionParam:Erp_Tablesets_PartOprActionParamRow[],
   PartOprMachParam:Erp_Tablesets_PartOprMachParamRow[],
   PartCOPart:Erp_Tablesets_PartCOPartRow[],
   PartMtlRefDes:Erp_Tablesets_PartMtlRefDesRow[],
   PartStage:Erp_Tablesets_PartStageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartCOPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
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
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the parent Part should be used as the primary costing method for the co-part  */  
   PrimaryCost:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   EnablePreventSugg:boolean,
   PartMasterPart:boolean,
   ProcessMode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartMtlAttchRow{
   Company:string,
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

export interface Erp_Tablesets_PartMtlInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Parent Part number to which this material item is a component of  */  
   PartNum:string,
      /**  Revision number of the part that this material item is a component of.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  */  
   MtlSeq:number,
      /**  A sequence number that uniquely identifies the PartMtlInsp record within the Part material  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
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

export interface Erp_Tablesets_PartMtlRefDesRow{
      /**  Company Identifier.  */  
   Company:string,
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
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartMtlRestrictSubstRow{
      /**  Company Identifier.  */  
   Company:string,
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
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   RestrictionDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SubstanceDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartMtlRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
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
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   RestrictionDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartMtlRow{
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
      /**  Quantity per parent  */  
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
      /**  Material comments specific to this manufacturing process. These comments copied to Jobs/Quotes when pulled from BOM. ( See  */  
   MfgComment:string,
      /**  Indicates if these comments should override the comments defined in the part master. It controls how the MfgComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the PartMtl.MfgComments will be appended on to the Part.MfgComments when written to the Job/Quote material record.  */  
   OverRideMfgComments:boolean,
      /**   Material comments specific to a manufacturing process. These comments (and optionally the comments from Part Master) are  copied to Jobs/Quotes when the BOM is pulled.
( See OverRidePurComments )  */  
   PurComment:string,
      /**  Indicates if these comments should override the comments defined in the part master. It controls how the PurComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the PartMtl.PurComments will be appended on to the Part.PurComments when written to the Job/Quote material record.  */  
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
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Site reference that requires this part in the current bill of Materials  */  
   ReqdInPlant:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  A material record can be related to a specific operation by stage. This field contains the JobOper.StageNumber of the operation that it is related to.  */  
   RelatedStage:string,
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
      /**  Rule Tag  */  
   RuleTag:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  This is relevant for assemblies (Part.Method = Yes). Indicates if the sub-assemby can be spawned off to a different job.  Can be true only if PullAsAsm = true.  */  
   PlanAsAsm:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If checked this indicates that serial numbers from the job material/subassembly are going to be reassigned as the serial number of the  parent’s assembly.  */  
   ReassignSNAsm:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
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
      /**  Weight Measurement  */  
   CNWeightMeasurement:boolean,
      /**  Required Qty  */  
   CNRequiredQty:number,
      /**  Consumed Qty  */  
   CNConsumedQty:number,
      /**  UOM  */  
   CNUOM:string,
      /**  Planning Percent  */  
   PlanningPct:number,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   MtlRevisionNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
   ExpandTree:boolean,
   GeneratedRuleTag:string,
      /**  The material part number mfg comment.  */  
   MtlPartNumMfgComment:string,
      /**  The material part number purchase comment.  */  
   MtlPartNumPurComment:string,
      /**   Material Revision Status determined against AS OF DATE
Possible Values are: EffectiveApprovedAsOfDate = 1, EffectiveNotApprovedAsOfDate = 2, FutureEffectiveApprovedAsOfDate = 3, FutureEffectiveNotApprovedAsOfDate = 4, Unknown = 5  */  
   MtlRevisionStatus:number,
      /**  Related operation description.  */  
   OpDesc:string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
   SalvageBaseUOM:string,
      /**  The display unit of measure for the qty/parent field.  */  
   DspUnitMeasure:string,
   SalvEnableAttSetSearch:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   PlanningNumberOfPiecesDisp:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   SalvagePlanningNumberOfPiecesDisp:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   APSSchedulerNameAPSSchedulerName:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   MtlPartNumPricePerCode:string,
   MtlPartNumSellingFactor:number,
   MtlPartNumTrackSerialNum:boolean,
   MtlPartNumPartDescription:string,
   MtlPartNumIUM:string,
   MtlPartNumTrackLots:boolean,
   MtlPartNumSalesUM:string,
   MtlPartNumTrackDimension:boolean,
   MtlPartNumTrackInventoryAttributes:boolean,
   MtlPartNumAttrClassID:string,
   MtlPartNumTypeCode:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   SalvagePartNumTrackLots:boolean,
   SalvagePartNumTrackDimension:boolean,
   SalvagePartNumSalesUM:string,
   SalvagePartNumTrackInventoryAttributes:boolean,
   SalvagePartNumAttrClassID:string,
   SalvagePartNumPartDescription:string,
   SalvagePartNumIUM:string,
   SalvagePartNumTrackSerialNum:boolean,
   SalvagePartNumPricePerCode:string,
   SalvagePartNumSellingFactor:number,
   SalvDynAttrValueSetDescription:string,
   SalvDynAttrValueSetShortDescription:string,
   StageNoDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOpDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the PartOpr this record is linked to.  System assigned.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  System assigned.  */  
   RevisionNum:string,
      /**  Uniquely identifies the PartOpDtl within the OpMaster.  */  
   OprSeq:number,
      /**  Uniquely identifies an PartOpDtl.  System assigned.  */  
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
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  Description is initially created when the PartOpDtl is created.   If the PartOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   OpDtlDesc:string,
      /**  Parent Alternate Routing method of this part operation.  */  
   ParentAltMethod:string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentOprSeq:number,
      /**  Indicates the parent operation detail sequence.  */  
   ParentOpDtlSeq:number,
      /**  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  */  
   ConcurrentCapacity:number,
      /**  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  */  
   DailyProdRate:number,
      /**  Duplicated from PartOper.SetupCrewSize.  The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  Duplicated from PartOper.SetupCrewSize.  Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
   OprSeqAPSSchedulerName:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
      /**  Resource description  */  
   ResourceDesc:string,
      /**  Capability description  */  
   CapabilityDesc:string,
      /**  Resource Group description  */  
   ResourceGrpDesc:string,
   BitFlag:number,
   CapabilityIDDescription:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumPricePerCode:string,
   PartNumIUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOprActionParamRow{
      /**  Company Identifier.  */  
   Company:string,
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
      /**  Data type of Action Parameter.  */  
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

export interface Erp_Tablesets_PartOprActionRow{
      /**  Company Identifier.  */  
   Company:string,
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

export interface Erp_Tablesets_PartOprAttchRow{
   Company:string,
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

export interface Erp_Tablesets_PartOprInspRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  */  
   OprSeq:number,
      /**  A sequence number that uniquely identifies the PartOprInsp ecord within the Part operation  */  
   PlanSeq:number,
      /**  The inspection plan part number (configurator part number).  */  
   InspPlanPartNum:string,
      /**  The specification ID.  Must be valid in the SpecHed table.  */  
   SpecID:string,
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

export interface Erp_Tablesets_PartOprMachParamRow{
      /**  Company  */  
   Company:string,
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
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
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

export interface Erp_Tablesets_PartOprRestrictSubstRow{
      /**  Company Identifier.  */  
   Company:string,
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
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   RestrictionDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumRevDescription:string,
   SubstanceDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOprRestrictionRow{
      /**  Company Identifier.  */  
   Company:string,
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
   PartNumPartDescription:string,
   PartNumPricePerCode:string,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   RestrictionDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartOprRow{
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
      /**  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (PartOpr.PartNum).  */  
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
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
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
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  */  
   LaborEntryMethod:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary PartOpDtl to be used for setup.  The setup time for the operation is determined on the PartOpDtl.
If <> 0, must identify a valid PartOpDtl.  The PartOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary PartOpDtl to be used for production.  The production run time for the operation is determined on the PartOpDtl.
If <> 0, must identify a valid PartOpDtl.  The PartOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  1 is the Primary Routing Group  */  
   RtgGroup:number,
      /**  Alternate Routing method for the part revision.  */  
   AltMethod:string,
      /**  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  */  
   BaseMethodOverridden:boolean,
      /**  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  */  
   StageNumber:string,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Parent Alternate Routing method of this part operation.  */  
   ParentAltMethod:string,
      /**  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  */  
   ParentOprSeq:number,
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
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
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
      /**  SubRevisionNum  */  
   SubRevisionNum:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
      /**  Auto receive?  */  
   AutoReceive:boolean,
   DspBillAddr:string,
   OpStdDescription:string,
      /**  Setup hours per machine.  */  
   SetHoursPerMach:number,
      /**  Final Operation?  */  
   FinalOpr:boolean,
   EnableAttributeSetSearch:boolean,
      /**  Description is initially created when the PartOpDtl is created. If the PartOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimaryProdOpDtlDesc:string,
      /**  Description is initially created when the PartOpDtl is created. If the PartOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimarySetupOpDtlDesc:string,
   BitFlag:number,
   AnalysisCdDescription:string,
   APSSchedulerNameAPSSchedulerName:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   OpCodeOpDesc:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   SetupGroupDescription:string,
   StageNoDescription:string,
   SubPartNumTrackInventoryAttributes:boolean,
   SubPartNumPricePerCode:string,
   SubPartNumTrackDimension:boolean,
   SubPartNumTrackSerialNum:boolean,
   SubPartNumSellingFactor:number,
   SubPartNumIUM:string,
   SubPartNumTrackLots:boolean,
   SubPartNumPartDescription:string,
   SubPartNumSalesUM:string,
   SubPartNumAttrClassID:string,
   VendorNumDefaultFOB:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorNumAddress1:string,
   VendorNumName:string,
   VendorNumZIP:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumTermsCode:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevAttchRow{
   Company:string,
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

export interface Erp_Tablesets_PartRevRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as part of the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  */  
   RevisionNum:string,
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
      /**  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  */  
   Method:boolean,
      /**   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  Holds the internal object id of pdm parts.  */  
   PDMObjID:string,
      /**  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  */  
   Configured:boolean,
      /**  If set to TRUE then the revision can be configured in StoreFront.  */  
   WebConfigured:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  Alternate Routing method to be used for this revision, and is used as part of the primary key  */  
   AltMethod:string,
      /**  The description of the alternate method.  */  
   AltMethodDesc:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The alternate method of the parent this method inherits from.  */  
   ParentAltMethod:string,
      /**  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  */  
   UseStaging:boolean,
      /**  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  */  
   UseAltRevForParts:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  External Configurator  */  
   ExtConfig:boolean,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Is the part for this revision a global part  */  
   PcGlobalPart:boolean,
      /**  If a configuration is created for this revision, is it marked as enterprise configurator  */  
   PcEntprsConf:boolean,
      /**  Marks the Part Revision as a global Revision, available to be sent out to other companies  */  
   GlobalRev:boolean,
      /**  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  */  
   RoughCutCode:string,
      /**  The inspection plan part number (configurator part number) to use for RMA processing for this part.  */  
   RMAInspPlan:string,
      /**  The specification ID to use for RMA processing for this part.  */  
   RMASpecID:string,
      /**  The default sample size to use for RMA processing for this part  */  
   RMASampleSize:number,
      /**  Percentage of quantity to be inspected for RMA processing of this part  */  
   RMASampleSizePct:number,
      /**  The part number used to identify the configured part number that this part revision was created from  */  
   BasePartNum:string,
      /**  The revision number used to identify the configured part revision this part number was generated from.  */  
   BaseRevisionNum:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  RegenConfig  */  
   RegenConfig:boolean,
      /**  SIValuesGroupSeq  */  
   SIValuesGroupSeq:number,
      /**  SIValuesHeadNum  */  
   SIValuesHeadNum:number,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  */  
   ProcessMode:string,
      /**  DefaultConfigPart  */  
   DefaultConfigPart:boolean,
      /**  Number of COPart required in the Revision  */  
   CoPartsReqQty:number,
      /**  Material Cost Factor  */  
   MtlCostPct:number,
      /**  Labor Cost Factor  */  
   LaborCostPct:number,
      /**  Number of COParts per Operation  */  
   CoPartsPerOp:number,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Customs BOM  */  
   CNCustomsBOM:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   ProcessMfgID:string,
      /**  Type of Process Manufacturing this revision is for: General, Site, Master.  */  
   ProcessMfgType:string,
      /**  Description of Process Manufacturing revision.  */  
   ProcessMfgDescription:string,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The last Group to modify this Revision for Recipe Authoring.  */  
   ProcessMfgLastGroupID:string,
      /**  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  */  
   ECPCEnabled:boolean,
   DisableApproved:boolean,
      /**  Name of ECO Group that this part is checked out to  */  
   ECOGroup:string,
      /**  This field will be set to true if two or more ECOCoParts records exist for the revision.  */  
   HasCoParts:boolean,
   ParentAltMethodDesc:string,
      /**  Part Number of the Parent Part  */  
   ParentPartNum:string,
      /**  Revision number  of Parent Part.  */  
   ParentRevisionNum:string,
   ProdCode:string,
      /**   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  */  
   RevStatusAsOfDate:number,
   SpecHedDescription:string,
      /**  Last date that this Revison is effective.  (Next Rev Effective date - 1)  */  
   vDate:string,
   vQty:number,
   Class:string,
   NonStock:boolean,
      /**  Indicates that the PartRev is the root node in the tree  */  
   IsRootNode:boolean,
      /**  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  */  
   EngineeringApproved:boolean,
   BitFlag:number,
   InspPlanDescription:string,
   PartDescriptionTrackDimension:boolean,
   PartDescriptionSellingFactor:number,
   PartDescriptionPartDescription:string,
   PartDescriptionIUM:string,
   PartDescriptionTrackLots:boolean,
   PartDescriptionPricePerCode:string,
   PartDescriptionSalesUM:string,
   PartDescriptionTrackSerialNum:boolean,
   PartDescriptionTypeCode:string,
   PcStatusConfigType:string,
   PlantName:string,
   RoughCutParamDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartStageRow{
      /**  Company Identifier.  */  
   Company:string,
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
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
      @param ipUseDefaultMethod
      @param ipAsOfDate
      @param ipCompleteTree
   */  
export interface GetAllAlternateTrees_input{
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  For partrev records other than the first one,
            would you like to use the default alternate method or the inputted one?  */  
   ipUseDefaultMethod:boolean,
      /**  The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
}

export interface GetAllAlternateTrees_output{
   returnObj:Erp_Tablesets_BomSearchTableset[],
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipProcessMfgID
      @param ipUseDefaultMethod
      @param ipAsOfDate
      @param ipCompleteTree
   */  
export interface GetDatasetForTreeByProcessMfgID_input{
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  The Alternate Method to return data for.  */  
   ipProcessMfgID:string,
      /**  For partrev records other than the first one, would you like to use the default alternate method or the inputted one?  */  
   ipUseDefaultMethod:boolean,
      /**  The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
}

export interface GetDatasetForTreeByProcessMfgID_output{
   returnObj:Erp_Tablesets_BomSearchTableset[],
}

   /** Required : 
      @param asOfDate
      @param partNum
      @param revisionNum
      @param altMethod
      @param isRootNode
   */  
export interface GetDatasetForTreeWithPartValidation_input{
      /**  As Of Date  */  
   asOfDate:string,
      /**  Part  */  
   partNum:string,
      /**  Revision  */  
   revisionNum:string,
      /**  Alt Method  */  
   altMethod:string,
      /**  Indicates if this is the root part/rev in the tree  */  
   isRootNode:boolean,
}

export interface GetDatasetForTreeWithPartValidation_output{
   returnObj:Erp_Tablesets_BomSearchTableset[],
parameters : {
      /**  output parameters  */  
   effectiveRevisionMessage:string,
   effectiveRevisionSubAsmMessage:string,
}
}

   /** Required : 
      @param ipPartNum
      @param ipRevisionNum
      @param ipAltMethod
      @param ipUseDefaultMethod
      @param ipAsOfDate
      @param ipCompleteTree
   */  
export interface GetDatasetForTree_input{
      /**  The Part Number to return data for.  */  
   ipPartNum:string,
      /**  The Revision Number to return data for.  */  
   ipRevisionNum:string,
      /**  The Alternate Method to return data for.  */  
   ipAltMethod:string,
      /**  For partrev records other than the first one, would you like to use the default alternate method or the inputted one?  */  
   ipUseDefaultMethod:boolean,
      /**  The as of date for the revisions, what would this look as of this date  */  
   ipAsOfDate:string,
      /**  Would you like to retun a complete dataset for this group?  */  
   ipCompleteTree:boolean,
}

export interface GetDatasetForTree_output{
   returnObj:Erp_Tablesets_BomSearchTableset[],
}

   /** Required : 
      @param ipSourceRowID
      @param droppedAs
   */  
export interface GetPartNumSource_input{
   ipSourceRowID:string,
   droppedAs:string,
}

export interface GetPartNumSource_output{
      /**  PartNum  */  
   returnObj:string,
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
      @param PartNum
      @param RevNum
      @param AltMethod
   */  
export interface PartRevExists_input{
      /**  Part ID  */  
   PartNum:string,
      /**  Revision ID  */  
   RevNum:string,
      /**  AltMethod  */  
   AltMethod:string,
}

export interface PartRevExists_output{
   returnObj:boolean,
}

