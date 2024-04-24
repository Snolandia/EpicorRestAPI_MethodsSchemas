import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.OrderJobWizSvc
// Description: JWJobHead
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", {
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



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/getNextOpDtlSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateJobs
   Description: This method creates job for selected orderdtls and/or orderrels.
This method will process any and all records where the ttJWJobOrderDtl.JobChkBox or
ttJWOrderRel.RelJobChkBox is set to true.
This method will also process the getDetails, Schedule and Release booleans.
   OperationID: CreateJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/CreateJobs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMatrix
   Description: To retrieve the OrdJobWiz dataset for a given part number.
This dataset consists of the Order Detail lines that are of type 'make' and thier
related releases. The dataset also includes open jobs for any part in the detail,
The client my need to filter the job dataset to represent only the jobs relevant to the
part on the detail. Index constraints on the xsd, did not allow me to do that in the BL.
   OperationID: GetMatrix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatrix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatrix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMatrix(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/GetMatrix", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Link
   Description: Creates link between selected release and selected job .
   OperationID: Link
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Link_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Link_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Link(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/Link", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectAll
   Description: This method processes the select all, getallmethod, sheduleall and releaseall fields
in the ttJWJobOrderDtl record. If any of the values in these fields change, this
method must be invoked in order for that change to be refelcted to the database.
Notes:
ttJWJobOrderDtl.Selectall = Set all values of Job checkbox to true for all lines in the Order Lines
Grid EXCEPT whre partID is an MRP part OR any release line for the detail
line linked to a job.
            
ttJWJobOrderDtl.DetailChkBox = Get All methods for all dtl lines, Selectall must be checked
ttJWJobOrderDtl.ScheduleAll  = Schedule all jobs, DetailChkBox must be checked
ttJWJobOrderDtl.ReleaseAll   = Release all jobs,  ScheduleAll  must be checked
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/SelectAll", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnLink
   Description: Unlink releases to Jobs .
   OperationID: UnLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnLink(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/UnLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateJobs
   Description: Gather all of the parts that are flagged to create jobs, and display the
ones in a message that won't be getting details.
   OperationID: ValidateJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/ValidateJobs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPlantConfCtrlUse3rdPartySched
   Description: Get the Use3rdPartySched field from PlantConfCtrl table.
   OperationID: GetPlantConfCtrlUse3rdPartySched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantConfCtrlUse3rdPartySched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlantConfCtrlUse3rdPartySched(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/GetPlantConfCtrlUse3rdPartySched", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface CreateJobs_input{
   ds:Erp_Tablesets_OrderJobWizTableset[],
}

export interface CreateJobs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderJobWizTableset[],
   pErrorMessages:string,
}
}

export interface Erp_Tablesets_JWJobHeadRow{
   Company:string,
   JobNum:string,
   ProdQty:number,
   ReqDueDate:string,
   StartDate:string,
   DueDate:string,
   JobReleased:boolean,
   SchedLocked:boolean,
   JobSources:string,
   PartNum:string,
   SelectedLinkJob:boolean,
   IUM:string,
      /**  Saves the ContractID value from JobHead  */  
   ContractID:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JWJobOrderDtlRow{
   Company:string,
   DocUnitPrice:number,
   IUM:string,
   LineDesc:string,
   NeedByDate:string,
   OrderLine:number,
   OrderNum:number,
   OrderQty:number,
   PartNum:string,
   RequestDate:string,
   RevisionNum:string,
   SellingQuantity:number,
   UnitPrice:number,
   SellingFactor:number,
   JobChkBox:boolean,
   DetailChkBox:boolean,
   ReleaseChkBox:boolean,
   ScheduleChkBox:boolean,
   MrpPart:boolean,
   NonStock:boolean,
   QuoteNum:number,
   QuoteLine:number,
   TotOnHand:number,
   TotReserved:number,
   TotAvail:number,
   InPartTable:boolean,
   ApprovedPartRev:boolean,
   HasLinkedReleases:boolean,
   SellingFactorDirection:string,
      /**  Tells if the PartRev reord for the part is approved  */  
   ApprovedMethod:boolean,
      /**  Holds the BasePartNum value from OrderDtl  */  
   BasePartNum:string,
      /**  Default Alternate Method for the current PartNum  */  
   DefaultAltMethod:string,
      /**  Holds a logical value that will tell if the OrderDtl line is configurable, this field is set in the buildTempTables procedure.  */  
   IsConfig:boolean,
      /**  Tells if there is a Quote Linked to this record  */  
   LinkedQuote:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   TotDemand:number,
      /**  If the OrderDtl record is flagged as LinkToContract  */  
   LinkToContract:boolean,
      /**  Save the ContractID related to the Sales Order Detail.  */  
   ContractID:string,
      /**  Indicates if inventory for the part is tracked at the attribute level. This requires Advanced Unit of Measure license.  */  
   TrackInventoryAttributes:boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
   TrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JWOrderRelRow{
   Company:string,
   RelSelectChkBox:boolean,
   RelDetailChkBox:boolean,
   RelScheduleChkBox:boolean,
   OrderNum:number,
   OrderLine:number,
   NeedByDate:string,
   OurJobQty:number,
   ReqDate:string,
   OrderRelNum:number,
   JobNum:string,
   Make:boolean,
   WarehouseCode:string,
   TargetJobNum:string,
   TargetAssemblySeq:number,
   TargetMtlSeq:number,
   SellingReqQty:number,
   QuoteNum:number,
   QuoteLine:number,
   OrderRelROWID:string,
   RelJobChkBox:boolean,
   RelReleaseChkBox:boolean,
   UM:string,
   JobsAvail:boolean,
   LineJobCheckBox:boolean,
   InPartTable:boolean,
      /**  Base Part, comes from the OrderDtl.BasePartNum record  */  
   BasePartNum:string,
      /**  Default Alternate Method for the parent OrderDtl of this release  */  
   DefaultAltMethod:string,
      /**  Tells if the PartRev reord for the part is approved  */  
   LineIsConfig:boolean,
      /**  Saves the value if the Order Release is flagged as Link To Contract  */  
   LinkToContract:boolean,
      /**  Saves the value of the ContractID related to the Order Release  */  
   ContractID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Partnum from OrderDtl  */  
   PartNum:string,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderJobWizTableset{
   JWJobHead:Erp_Tablesets_JWJobHeadRow[],
   JWJobOrderDtl:Erp_Tablesets_JWJobOrderDtlRow[],
   JWOrderRel:Erp_Tablesets_JWOrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param CurOrderNum
      @param CurOrderLine
      @param CurOrderRelNum
   */  
export interface GetMatrix_input{
      /**  OrderNum to be processed  */  
   CurOrderNum:number,
      /**  Optional, Passing in when comming from Job Planner to valid Suggestion  */  
   CurOrderLine:number,
      /**  Optional, Passing in when comming from Job Planner to valid Suggestion  */  
   CurOrderRelNum:number,
}

export interface GetMatrix_output{
   returnObj:Erp_Tablesets_OrderJobWizTableset[],
}

export interface GetPlantConfCtrlUse3rdPartySched_output{
      /**  bool: the value  */  
   returnObj:boolean,
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
   */  
export interface Link_input{
   ds:Erp_Tablesets_OrderJobWizTableset[],
}

export interface Link_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderJobWizTableset[],
}
}

   /** Required : 
      @param curOrderNum
      @param insavedSelectAll
      @param insavedgetallmethods
      @param insavedScheduleAll
      @param insavedReleaseAll
   */  
export interface SelectAll_input{
      /**  Order Number  */  
   curOrderNum:number,
   insavedSelectAll:boolean,
      /**  Get All Methods  */  
   insavedgetallmethods:boolean,
      /**  Schedule All  */  
   insavedScheduleAll:boolean,
      /**  Release All  */  
   insavedReleaseAll:boolean,
}

export interface SelectAll_output{
   returnObj:Erp_Tablesets_OrderJobWizTableset[],
}

   /** Required : 
      @param ds
   */  
export interface UnLink_input{
   ds:Erp_Tablesets_OrderJobWizTableset[],
}

export interface UnLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderJobWizTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateJobs_input{
   ds:Erp_Tablesets_OrderJobWizTableset[],
}

export interface ValidateJobs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OrderJobWizTableset[],
   WarnMsg:string,
}
}

   /** Required : 
      @param ipCompany
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOprSeq
   */  
export interface getNextOpDtlSeq_input{
   ipCompany:string,
   ipJobNum:string,
   ipAssemblySeq:number,
   ipOprSeq:number,
}

export interface getNextOpDtlSeq_output{
   returnObj:number,
}

