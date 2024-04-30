import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.OverrideSchedOrdersSvc
// Description: OverrideSchedOrdersSvc Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/$metadata", {
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
   Summary: Invoke method DeleteRec
   Description: Delete current record and reset values (Job Number - number or list
   OperationID: DeleteRec
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRec(requestBody:DeleteRec_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRec_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/DeleteRec", {
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
         resolve(data as DeleteRec_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadOverrideSched
   Description: /// Populates ttOverrideSchedOrders table from JobHead, PatchFld
///
   OperationID: LoadOverrideSched
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadOverrideSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadOverrideSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadOverrideSched(requestBody:LoadOverrideSched_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadOverrideSched_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/LoadOverrideSched", {
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
         resolve(data as LoadOverrideSched_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MultiJobUpdateSchedPri
   Description: Update default information based on the warehouse changing
   OperationID: MultiJobUpdateSchedPri
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MultiJobUpdateSchedPri_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MultiJobUpdateSchedPri_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MultiJobUpdateSchedPri(requestBody:MultiJobUpdateSchedPri_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MultiJobUpdateSchedPri_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/MultiJobUpdateSchedPri", {
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
         resolve(data as MultiJobUpdateSchedPri_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateSchedPri
   Description: Update default information based on the warehouse changing
   OperationID: UpdateSchedPri
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateSchedPri_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSchedPri_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSchedPri(requestBody:UpdateSchedPri_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateSchedPri_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/UpdateSchedPri", {
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
         resolve(data as UpdateSchedPri_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCalculateGlobalSchedulingLastRun
   Description: Get multi job Flag used in the Last Run of the Scheduling
   OperationID: GetCalculateGlobalSchedulingLastRun
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCalculateGlobalSchedulingLastRun_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCalculateGlobalSchedulingLastRun_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCalculateGlobalSchedulingLastRun(requestBody:GetCalculateGlobalSchedulingLastRun_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCalculateGlobalSchedulingLastRun_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/GetCalculateGlobalSchedulingLastRun", {
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
         resolve(data as GetCalculateGlobalSchedulingLastRun_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBackwards
   Description: Column Changed for Backwards
   OperationID: OnChangeBackwards
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBackwards_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBackwards_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBackwards(requestBody:OnChangeBackwards_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBackwards_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/OnChangeBackwards", {
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
         resolve(data as OnChangeBackwards_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMultiJobSchedSeq
   Description: Column Changed for MultiJobSchedSeq
   OperationID: OnChangeMultiJobSchedSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMultiJobSchedSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMultiJobSchedSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMultiJobSchedSeq(requestBody:OnChangeMultiJobSchedSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMultiJobSchedSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/OnChangeMultiJobSchedSeq", {
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
         resolve(data as OnChangeMultiJobSchedSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingSchedSeq
   Description: On changing of MultiJobSchedSeq
   OperationID: OnChangingSchedSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingSchedSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSchedSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSchedSeq(requestBody:OnChangingSchedSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingSchedSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/OnChangingSchedSeq", {
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
         resolve(data as OnChangingSchedSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadOverrideSchedOrderView
   Description: Add rows from the JobHead dataset to the OverrideSchedOrders dataset.
   OperationID: LoadOverrideSchedOrderView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadOverrideSchedOrderView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadOverrideSchedOrderView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadOverrideSchedOrderView(requestBody:LoadOverrideSchedOrderView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadOverrideSchedOrderView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/LoadOverrideSchedOrderView", {
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
         resolve(data as LoadOverrideSchedOrderView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadOverrideSchedOrderViewList
   OperationID: LoadOverrideSchedOrderViewList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadOverrideSchedOrderViewList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadOverrideSchedOrderViewList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadOverrideSchedOrderViewList(requestBody:LoadOverrideSchedOrderViewList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadOverrideSchedOrderViewList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/LoadOverrideSchedOrderViewList", {
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
         resolve(data as LoadOverrideSchedOrderViewList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshOverrideSchedOrderView
   Description: Custom Refresh of jobs
   OperationID: RefreshOverrideSchedOrderView
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshOverrideSchedOrderView_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshOverrideSchedOrderView_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshOverrideSchedOrderView(requestBody:RefreshOverrideSchedOrderView_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshOverrideSchedOrderView_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/RefreshOverrideSchedOrderView", {
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
         resolve(data as RefreshOverrideSchedOrderView_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SeqIsDecimal
   Description: determine if multiJobSchedSeq is a decimal
   OperationID: SeqIsDecimal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SeqIsDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SeqIsDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SeqIsDecimal(requestBody:SeqIsDecimal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SeqIsDecimal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.OverrideSchedOrdersSvc/SeqIsDecimal", {
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
         resolve(data as SeqIsDecimal_output)
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
   /** Required : 
      @param ipJobNum
   */  
export interface DeleteRec_input{
      /**  Job Number  */  
   ipJobNum:string,
}

export interface DeleteRec_output{
}

export interface Erp_Tablesets_JobAsmRefDesRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   RefDes:string,
   RefDesSeq:number,
   MtlPartNum:string,
   Side:string,
   XLocation:number,
   YLocation:number,
   ZLocation:number,
   Rotation:number,
   Description:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Erp_Tablesets_JobAsmblAttchRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobAsmblInspRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   PlanSeq:number,
   InspPlanPartNum:string,
   InspPlanRevNum:string,
   SpecID:string,
   SpecRevNum:string,
   SysRevID:number,
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobAsmblRestrictSubstRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   RestrictionTypeID:string,
   SubstanceID:string,
   Weight:number,
   WeightUOM:string,
   Manual:boolean,
   SysRevID:number,
   SysRowID:string,
   PartNum:string,
   BitFlag:number,
   JobNumPartDescription:string,
   RestrictionDescription:string,
   SubstanceDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobAsmblRestrictionRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   RestrictionTypeID:string,
   PartNum:string,
   Manual:boolean,
   RollupType:string,
   Compliance:string,
   ComplianceDate:string,
   LastRollUp:string,
   BuiltCompliance:string,
   BuiltComplianceDate:string,
   BuiltLastRollUp:string,
   SysRevID:number,
   SysRowID:string,
   Weight:boolean,
   EnableRollUpType:boolean,
   BitFlag:number,
   JobNumPartDescription:string,
   RestrictionDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobAsmblRow{
   Company:string,
   JobComplete:boolean,
   JobNum:string,
   AssemblySeq:number,
   PartNum:string,
   Description:string,
   RevisionNum:string,
   QtyPer:number,
   IUM:string,
   RequiredQty:number,
   PullQty:number,
   WarehouseCode:string,
   MtlBurRate:number,
   EstUnitCost:number,
   EstMtlBurUnitCost:number,
   OverRunQty:number,
   StartDate:string,
   StartHour:number,
   DueDate:string,
   DueHour:number,
   Parent:number,
   PriorPeer:number,
   NextPeer:number,
   Child:number,
   TotalCost:number,
   MtlBurCost:number,
   IssuedQty:number,
   DrawNum:string,
   IssuedComplete:boolean,
   CommentText:string,
   InCopyList:boolean,
   BomSequence:number,
   BomLevel:number,
   WIStartDate:string,
   WIStartHour:number,
   WIDueDate:string,
   WIDueHour:number,
   TLALaborCost:number,
   TLABurdenCost:number,
   TLAMaterialCost:number,
   TLASubcontractCost:number,
   TLAMtlBurCost:number,
   TLASetupHours:number,
   TLAProdHours:number,
   TLELaborCost:number,
   TLEBurdenCost:number,
   TLEMaterialCost:number,
   TLESubcontractCost:number,
   TLEMtlBurCost:number,
   TLESetupHours:number,
   TLEProdHours:number,
   LLALaborCost:number,
   LLABurdenCost:number,
   LLAMaterialCost:number,
   LLASubcontractCost:number,
   LLAMtlBurCost:number,
   LLASetupHours:number,
   LLAProdHours:number,
   LLELaborCost:number,
   LLEBurdenCost:number,
   LLEMaterialCost:number,
   LLESubcontractCost:number,
   LLEMtlBurCost:number,
   LLESetupHours:number,
   LLEProdHours:number,
   AutoRecOpr:number,
   FinalOpr:number,
   FindNum:string,
   ReceivedToStock:number,
   Plant:string,
   Direct:boolean,
   RelatedOperation:number,
   TLAMaterialLabCost:number,
   TLAMaterialMtlCost:number,
   TLAMaterialSubCost:number,
   TLAMaterialBurCost:number,
   LLAMaterialLabCost:number,
   LLAMaterialMtlCost:number,
   LLAMaterialSubCost:number,
   LLAMaterialBurCost:number,
   TotalMtlMtlCost:number,
   TotalMtlLabCost:number,
   TotalMtlSubCost:number,
   TotalMtlBurCost:number,
   CallNum:number,
   CallLine:number,
   RestoreFlag:string,
   AnalysisCode:string,
   LastConfigDate:string,
   LastConfigTime:number,
   LastConfigUserID:string,
   OrigRequiredQty:number,
   UserMapData:string,
   WhseAllocFlag:boolean,
   TLAMaterialMtlBurCost:number,
   LLAMaterialMtlBurCost:number,
   TLAMfgCompLabCost:number,
   TLAMfgCompMtlCost:number,
   TLAMfgCompSubCost:number,
   TLAMfgCompBurCost:number,
   TLAMfgCompMtlBurCost:number,
   LLAMfgCompLabCost:number,
   LLAMfgCompMtlCost:number,
   LLAMfgCompSubCost:number,
   LLAMfgCompBurCost:number,
   LLAMfgCompMtlBurCost:number,
   Weight:number,
   WeightUOM:string,
   OrigMtlSeq:number,
   OrigRuleTag:string,
   ValRefDes:boolean,
   BasePartNum:string,
   BaseRevisionNum:string,
   EstMtlUnitCost:number,
   EstLbrUnitCost:number,
   EstBurUnitCost:number,
   EstSubUnitCost:number,
   PlanAsAsm:boolean,
   PAARef:string,
   PAAFirm:boolean,
   EstScrap:number,
   EstScrapType:string,
   SmartStringProcessed:boolean,
   SmartString:string,
   ReqRefDes:number,
   ReassignSNAsm:boolean,
   TLAODCCost:number,
   AssemblyMatch:string,
   JdfStatus:string,
   PressDevice:string,
   DigitalFileName:string,
   PrepressJobName:string,
   JdfPrepressAction:string,
   SendToPress:boolean,
   RemovedFromPlan:boolean,
   SendToPressInitiator:number,
   OperationType:number,
   SendToPrePress:boolean,
   GroupSeq:number,
   SysRevID:number,
   SysRowID:string,
   PartPlanInfo:string,
   OrigStructTag:string,
   ContractID:string,
   LinkToContract:boolean,
   PCLinkRemoved:boolean,
   ExternalMESSyncRequired:boolean,
   ExternalMESLastSync:string,
   AttributeSetID:number,
   PlanningNumberOfPieces:number,
   KBConfigProdID:number,
   AvailableQty:number,
   bUseAvailQty:boolean,
   ChildAssemblySeq:number,
   DispIUM:string,
   DisplayOrder:number,
   EnableAsmSplitCosts:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
   FirmProcEnable:boolean,
   FirmProcess:boolean,
   GetCostsFromInventory:boolean,
   GetCostsFromTemplate:boolean,
   ParentAssemblySeq:number,
   ParentDescription:string,
   ParentPartNum:string,
   ParentRev:string,
   PartExists:boolean,
   PartmasterPart:boolean,
   RDEndNum:number,
   RDPrefix:string,
   RDStartNum:number,
   RDSuffix:string,
   RelatedOperationDesc:string,
   ShowWarningBOMResequence:boolean,
   AddAsmAs:string,
   bAvailQty:number,
   EnableAttributeSetSearch:boolean,
   AttributeSetShortDescription:string,
   AttributeSetDescription:string,
   AttrClassID:string,
   TLATotalCost:number,
   TLETotalCost:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PlantName:string,
   WarehouseCodeDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobAuditRow{
   Company:string,
   JobNum:string,
   ChangeDate:string,
   ChangeTime:number,
   ChangedBy:string,
   ChangeDescription:string,
   SysRevID:number,
   SysRowID:string,
   DspChangeTime:string,
   BitFlag:number,
   JobNumPartDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobEntryTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   JobHeadAttch:Erp_Tablesets_JobHeadAttchRow[],
   JobAsmbl:Erp_Tablesets_JobAsmblRow[],
   JobAsmblAttch:Erp_Tablesets_JobAsmblAttchRow[],
   JobAsmblInsp:Erp_Tablesets_JobAsmblInspRow[],
   JobMtl:Erp_Tablesets_JobMtlRow[],
   JobMtlAttch:Erp_Tablesets_JobMtlAttchRow[],
   JobMtlInsp:Erp_Tablesets_JobMtlInspRow[],
   JobMtlRefDes:Erp_Tablesets_JobMtlRefDesRow[],
   JobMtlRestriction:Erp_Tablesets_JobMtlRestrictionRow[],
   JobMtlRestrictSubst:Erp_Tablesets_JobMtlRestrictSubstRow[],
   JobOper:Erp_Tablesets_JobOperRow[],
   JobOperAttch:Erp_Tablesets_JobOperAttchRow[],
   JobOperAction:Erp_Tablesets_JobOperActionRow[],
   JobOperActionParam:Erp_Tablesets_JobOperActionParamRow[],
   JobOperInsp:Erp_Tablesets_JobOperInspRow[],
   JobOperMachParam:Erp_Tablesets_JobOperMachParamRow[],
   JobOpDtl:Erp_Tablesets_JobOpDtlRow[],
   JobResources:Erp_Tablesets_JobResourcesRow[],
   JobOperRestriction:Erp_Tablesets_JobOperRestrictionRow[],
   JobOperRestrictSubst:Erp_Tablesets_JobOperRestrictSubstRow[],
   JobAsmblRestriction:Erp_Tablesets_JobAsmblRestrictionRow[],
   JobAsmblRestrictSubst:Erp_Tablesets_JobAsmblRestrictSubstRow[],
   JobAsmRefDes:Erp_Tablesets_JobAsmRefDesRow[],
   JobAudit:Erp_Tablesets_JobAuditRow[],
   JobPart:Erp_Tablesets_JobPartRow[],
   JobProd:Erp_Tablesets_JobProdRow[],
   JobStage:Erp_Tablesets_JobStageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobHeadAttchRow{
   Company:string,
   JobNum:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobHeadListRow{
   Company:string,
   JobClosed:boolean,
   ClosedDate:string,
   JobComplete:boolean,
   JobCompletionDate:string,
   JobEngineered:boolean,
   JobReleased:boolean,
   JobHeld:boolean,
   JobNum:string,
   PartNum:string,
   RevisionNum:string,
   DrawNum:string,
   PartDescription:string,
   ProdQty:number,
   IUM:string,
   StartDate:string,
   StartHour:number,
   DueDate:string,
   DueHour:number,
   ReqDueDate:string,
   JobCode:string,
   QuoteNum:number,
   QuoteLine:number,
   ProdCode:string,
   CommentText:string,
   ExpenseCode:string,
   InCopyList:boolean,
   WIName:string,
   WIStartDate:string,
   WIStartHour:number,
   Candidate:boolean,
   SchedCode:string,
   SchedLocked:boolean,
   ProjectID:string,
   WIPCleared:boolean,
   JobFirm:boolean,
   PersonList:string,
   PersonID:string,
   ProdTeamID:string,
   QtyCompleted:number,
   Plant:string,
   DatePurged:string,
   TravelerReadyToPrint:boolean,
   TravelerLastPrinted:string,
   StatusReadyToPrint:boolean,
   StatusLastPrinted:string,
   CallNum:number,
   CallLine:number,
   JobType:string,
   PhaseID:string,
   AnalysisCode:string,
   HDCaseNum:number,
   ProductionYield:boolean,
   EquipID:string,
   PlanNum:number,
   IssueTopicID1:string,
   ExternalMES:boolean,
   SysRowID:string,
   AttributeSetID:number,
   PersonIDName:string,
   SOExists:boolean,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   EquipOEM:string,
   EquipModel:string,
   EquipTypeID:string,
   EquipLocID:string,
   PMJob:boolean,
   EquipDescription:string,
   JobTypeName:string,
   SmartString:string,
   SmartStringProcessed:boolean,
   AttrClassID:string,
   AttrDescription:string,
   ShortDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobHeadListTableset{
   JobHeadList:Erp_Tablesets_JobHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobHeadRow{
   Company:string,
   JobClosed:boolean,
   ClosedDate:string,
   JobComplete:boolean,
   JobCompletionDate:string,
   JobEngineered:boolean,
   CheckOff1:boolean,
   CheckOff2:boolean,
   CheckOff3:boolean,
   CheckOff4:boolean,
   CheckOff5:boolean,
   JobReleased:boolean,
   JobHeld:boolean,
   SchedStatus:string,
   JobNum:string,
   PartNum:string,
   RevisionNum:string,
   DrawNum:string,
   PartDescription:string,
   ProdQty:number,
   IUM:string,
   StartDate:string,
   StartHour:number,
   DueDate:string,
   DueHour:number,
   ReqDueDate:string,
   JobCode:string,
   QuoteNum:number,
   QuoteLine:number,
   ProdCode:string,
   UserChar1:string,
   UserChar2:string,
   UserChar3:string,
   UserChar4:string,
   UserDate1:string,
   UserDate2:string,
   UserDate3:string,
   UserDate4:string,
   UserDecimal1:number,
   UserDecimal2:number,
   UserInteger1:number,
   UserInteger2:number,
   CommentText:string,
   ExpenseCode:string,
   InCopyList:boolean,
   WIName:string,
   WIStartDate:string,
   WIStartHour:number,
   WIDueDate:string,
   WIDueHour:number,
   Candidate:boolean,
   SchedCode:string,
   SchedLocked:boolean,
   ProjectID:string,
   WIPCleared:boolean,
   JobFirm:boolean,
   PersonList:string,
   PersonID:string,
   ProdTeamID:string,
   QtyCompleted:number,
   Plant:string,
   DatePurged:string,
   TravelerReadyToPrint:boolean,
   TravelerLastPrinted:string,
   StatusReadyToPrint:boolean,
   StatusLastPrinted:string,
   CallNum:number,
   CallLine:number,
   JobType:string,
   RestoreFlag:string,
   PhaseID:string,
   AnalysisCode:string,
   LockQty:boolean,
   HDCaseNum:number,
   ProcessMode:string,
   PlannedActionDate:string,
   PlannedKitDate:string,
   MSPTaskID:string,
   MSPPredecessor:string,
   UserMapData:string,
   ProductionYield:boolean,
   OrigProdQty:number,
   PreserveOrigQtys:boolean,
   NoAutoCompletion:boolean,
   NoAutoClosing:boolean,
   CreatedBy:string,
   CreateDate:string,
   WhseAllocFlag:boolean,
   OwnershipStatus:string,
   PDMObjID:string,
   ExportRequested:string,
   SplitMfgCostElements:boolean,
   XRefPartNum:string,
   XRefPartType:string,
   XRefCustNum:number,
   BasePartNum:string,
   BaseRevisionNum:string,
   RoughCutScheduled:boolean,
   EquipID:string,
   PlanNum:number,
   MaintPriority:string,
   SplitJob:boolean,
   NumberSource:boolean,
   CloseMeterReading:number,
   IssueTopicID1:string,
   IssueTopicID2:string,
   IssueTopicID3:string,
   IssueTopicID4:string,
   IssueTopicID5:string,
   IssueTopicID6:string,
   IssueTopicID7:string,
   IssueTopicID8:string,
   IssueTopicID9:string,
   IssueTopicID10:string,
   IssueTopics:string,
   ResTopicID1:string,
   ResTopicID2:string,
   ResTopicID3:string,
   ResTopicID4:string,
   ResTopicID5:string,
   ResTopicID6:string,
   ResTopicID7:string,
   ResTopicID8:string,
   ResTopicID9:string,
   ResTopicID10:string,
   ResTopics:string,
   Forward:boolean,
   SchedSeq:number,
   PAAExists:boolean,
   DtlsWithinLeadTime:boolean,
   GroupSeq:number,
   RoughCut:boolean,
   PlanGUID:string,
   PlanUserID:string,
   LastChangedBy:string,
   LastChangedOn:string,
   EPMExportLevel:number,
   JobWorkflowState:string,
   JobCSR:string,
   ExternalMES:boolean,
   SysRevID:number,
   SysRowID:string,
   LastExternalMESDate:string,
   LastScheduleDate:string,
   LastScheduleProc:string,
   SchedPriority:number,
   DaysLate:number,
   ContractID:string,
   ProjProcessed:boolean,
   SyncReqBy:boolean,
   CustName:string,
   CustID:string,
   IsCSRSet:boolean,
   UnReadyCostProcess:boolean,
   ProcSuspendedUpdates:string,
   ProjProcessedDate:string,
   PCLinkRemoved:boolean,
   ExternalMESSyncRequired:boolean,
   ExternalMESLastSync:string,
   EpicorFSA:boolean,
   KBConfigProdID:number,
   UseAdvancedStaging:boolean,
   AttributeSetID:number,
   PersonIDName:string,
   ReadyToFulfill:boolean,
   FSMSendTo:boolean,
   FSMServiceReportID:string,
   AdvanceLaborRate:boolean,
   dspReadyCostProcess:boolean,
   EnableJobEngineered:boolean,
   EnableJobFirm:boolean,
   EnableJobReleased:boolean,
   EnableMaterialStatus:boolean,
   EnableProject:boolean,
   EngineerAllowed:boolean,
   EquipLocDesc:string,
   ExtUpdated:boolean,
   FinalOpDueDate:string,
   FirmProcEnable:boolean,
   FirmProcess:boolean,
   HasPlanAsAsm:boolean,
   HeaderSensitive:boolean,
   IgnoreMtlConstraints:boolean,
   JobTypeName:string,
   KitTime:number,
   LockedQty:boolean,
   NewMeter:number,
   OldJobNum:string,
   OrderQty:number,
   PartmasterPart:boolean,
   PhaseDescription:string,
   PMJob:boolean,
   ProcessModeDescription:string,
   ReceiveTime:number,
   SmartString:string,
   SmartStringProcessed:boolean,
   SOExists:boolean,
   StockQty:number,
   ToFirm:boolean,
   XRefPartTypeDesc:string,
   ChangeDescription:string,
   ClearDataset:boolean,
   IsCoPart:boolean,
   PartRevProcessMfgID:string,
   PartRevProcessMfgType:string,
   SendToFSA:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   EquipMeterUOM:string,
   EquipSerialNum:string,
   EquipLocID:string,
   EquipPlant:string,
   EquipDescription:string,
   EquipBrand:string,
   EquipModel:string,
   EquipCurrentMeter:number,
   EquipTypeID:string,
   EquipOEM:string,
   ExpenseCodeDescription:string,
   HDCaseDescription:string,
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
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumLocationIDNumReq:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   PlantMaintPlant:string,
   ProdCodeDescription:string,
   ProdTeamIDDescription:string,
   ProdTeamIDName:string,
   ProjectIDDescription:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
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
   SchedCodeDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlAttchRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
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
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlInspRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   PlanSeq:number,
   InspPlanPartNum:string,
   InspPlanRevNum:string,
   SpecID:string,
   SpecRevNum:string,
   SysRevID:number,
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlRefDesRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   RefDes:string,
   RefDesSeq:number,
   MtlPartNum:string,
   Side:string,
   XLocation:number,
   YLocation:number,
   ZLocation:number,
   Rotation:number,
   Description:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlRestrictSubstRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   RestrictionTypeID:string,
   SubstanceID:string,
   Weight:number,
   WeightUOM:string,
   Manual:boolean,
   ExemptDate:string,
   ExemptCertificate:string,
   SysRevID:number,
   SysRowID:string,
   Exempt:boolean,
   MtlPartNum:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   RestrictionDescription:string,
   SubstanceDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlRestrictionRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   RestrictionTypeID:string,
   MtlPartNum:string,
   Manual:boolean,
   SysRevID:number,
   SysRowID:string,
   Weight:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   RestrictionDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlRow{
   Company:string,
   JobComplete:boolean,
   IssuedComplete:boolean,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   PartNum:string,
   Description:string,
   QtyPer:number,
   RequiredQty:number,
   IUM:string,
   LeadTime:number,
   RelatedOperation:number,
   MtlBurRate:number,
   EstMtlBurUnitCost:number,
   EstUnitCost:number,
   IssuedQty:number,
   TotalCost:number,
   MtlBurCost:number,
   ReqDate:string,
   WarehouseCode:string,
   SalvagePartNum:string,
   SalvageDescription:string,
   SalvageQtyPer:number,
   SalvageUM:string,
   SalvageMtlBurRate:number,
   SalvageUnitCredit:number,
   SalvageEstMtlBurUnitCredit:number,
   SalvageQtyToDate:number,
   SalvageCredit:number,
   SalvageMtlBurCredit:number,
   MfgComment:string,
   VendorNum:number,
   PurPoint:string,
   BuyIt:boolean,
   Ordered:boolean,
   PurComment:string,
   BackFlush:boolean,
   EstScrap:number,
   EstScrapType:string,
   FixedQty:boolean,
   FindNum:string,
   RevisionNum:string,
   SndAlrtCmpl:boolean,
   RcvInspectionReq:boolean,
   Plant:string,
   Direct:boolean,
   MaterialMtlCost:number,
   MaterialLabCost:number,
   MaterialSubCost:number,
   MaterialBurCost:number,
   SalvageMtlCredit:number,
   SalvageLbrCredit:number,
   SalvageBurCredit:number,
   SalvageSubCredit:number,
   APSAddResType:string,
   CallNum:number,
   CallLine:number,
   ProdCode:string,
   UnitPrice:number,
   BillableUnitPrice:number,
   DocBillableUnitPrice:number,
   ResReasonCode:string,
   PricePerCode:string,
   Billable:boolean,
   ShippedQty:number,
   DocUnitPrice:number,
   QtyStagedToDate:number,
   AddedMtl:boolean,
   MiscCharge:boolean,
   MiscCode:string,
   SCMiscCode:string,
   RFQNeeded:boolean,
   RFQVendQuotes:number,
   RFQNum:number,
   RFQLine:number,
   RFQStat:string,
   AnalysisCode:string,
   GlbRFQ:boolean,
   WhseAllocFlag:boolean,
   WIReqDate:string,
   Rpt1BillableUnitPrice:number,
   Rpt2BillableUnitPrice:number,
   Rpt3BillableUnitPrice:number,
   Rpt1UnitPrice:number,
   Rpt2UnitPrice:number,
   Rpt3UnitPrice:number,
   BaseRequiredQty:number,
   BaseUOM:string,
   Weight:number,
   WeightUOM:string,
   ReqRefDes:number,
   BasePartNum:string,
   BaseRevisionNum:string,
   SelectForPicking:boolean,
   StagingWarehouseCode:string,
   StagingBinNum:string,
   PickError:string,
   EstMtlUnitCost:number,
   EstLbrUnitCost:number,
   EstBurUnitCost:number,
   EstSubUnitCost:number,
   SalvageEstMtlUnitCredit:number,
   SalvageEstLbrUnitCredit:number,
   SalvageEstBurUnitCredit:number,
   SalvageEstSubUnitCredit:number,
   LoanedQty:number,
   BorrowedQty:number,
   ReassignSNAsm:boolean,
   GeneralPlanInfo:string,
   EstStdDescription:string,
   PricingUOM:string,
   RemovedFromPlan:boolean,
   IsPOCostingMaintained:boolean,
   EstStdType:number,
   POCostingFactor:number,
   PlannedQtyPerUnit:number,
   POCostingDirection:number,
   POCostingUnitVal:number,
   GroupSeq:number,
   SysRevID:number,
   SysRowID:string,
   OrigStructTag:string,
   OrigGroupSeq:number,
   ShowStatusIcon:string,
   ContractID:string,
   LinkToContract:boolean,
   StagingLotNum:string,
   PCLinkRemoved:boolean,
   ExternalMESSyncRequired:boolean,
   ExternalMESLastSync:string,
   LocationView:boolean,
   AttributeSetID:number,
   PlanningNumberOfPieces:number,
   SalvageAttributeSetID:number,
   SalvagePlanningNumberOfPieces:number,
   SalvagePlanningAttributeSetID:number,
   RelatedStage:string,
   SalvageRevisionNum:string,
   PartAllocQueueAction:string,
   ReadyToFulfill:boolean,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DisplayExtPrice:number,
   DisplayUnitPrice:number,
   DocDisplayExtPrice:number,
   DocDisplayUnitPrice:number,
   dspBuyIt:boolean,
   DspIUM:string,
   EnableBackflush:boolean,
   EnableBuyIt:boolean,
   EnableConfigure:boolean,
   EnableDirect:boolean,
   EnableFixedQty:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
   EnableRcvInspReq:boolean,
   EnableSndAlrtCmpl:boolean,
   EnableSplitCosts:boolean,
   EstCost:number,
   IPCaller:string,
   IsBaseCurrency:boolean,
   IsMtlConfigurationOn:boolean,
   IsMtlConfigureOn:boolean,
   IsMtlExtConfig:boolean,
   IsMtlRevisionApproved:boolean,
   PartExists:boolean,
   PlantList:string,
   PricePerCodeDescription:string,
   RDEndNum:number,
   RDPrefix:string,
   RDStartNum:number,
   RDSuffix:string,
   RelatedOperationDesc:string,
   RetainValues:boolean,
   Rpt1DisplayExtPrice:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayExtPrice:number,
   Rpt3DisplayUnitPrice:number,
   SalvageBaseUOM:string,
   ShowInspRqdImg:boolean,
   SubContract:boolean,
   AllowBackflushUncheck:boolean,
   EnableAttributeSetSearch:boolean,
   EnableSalvageAttributeSetSearch:boolean,
   PlanningNumberOfPiecesDisp:number,
   SalvagePlanningNumberOfPiecesDisp:number,
   SkipUnitPriceCalc:boolean,
   ErrorStatusDisplay:string,
   InPartAllocQueue:boolean,
   ShowFulfillmentQueueActions:boolean,
   SelectedForAction:boolean,
   AllocatedQty:number,
   ReservedQty:number,
   AvailableQty:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqPartNum:string,
   AssemblySeqDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   JobNumPartDescription:string,
   JobNumPartNum:string,
   MiscCodeDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PlantName:string,
   ProdCodeDescription:string,
   PurMiscCodeDescription:string,
   PurMiscCodeLCAmount:number,
   PurMiscCodeLCDisburseMethod:string,
   PurMiscCodeLCCurrencyCode:string,
   ReasonDescription:string,
   RFQLineLineDesc:string,
   SalvageAttributeSetIDDescription:string,
   SalvageAttributeSetIDShortDescription:string,
   SalvagePartNumPartDescription:string,
   SalvagePartNumPricePerCode:string,
   SalvagePartNumTrackInventoryByRevision:boolean,
   SalvagePartNumTrackSerialNum:boolean,
   SalvagePartNumTrackDimension:boolean,
   SalvagePartNumTrackInventoryAttributes:boolean,
   SalvagePartNumAttrClassID:string,
   SalvagePartNumSellingFactor:number,
   SalvagePartNumTrackLots:boolean,
   SalvagePartNumSalesUM:string,
   SalvagePartNumIUM:string,
   SCMiscCodeDescription:string,
   StageNoDescription:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorPPState:string,
   VendorPPAddress2:string,
   VendorPPCountry:string,
   VendorPPPrimPCon:number,
   VendorPPZip:string,
   VendorPPCity:string,
   VendorPPAddress1:string,
   VendorPPAddress3:string,
   VendorPPName:string,
   WarehouseCodeDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobOpDtlRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   OpDtlSeq:number,
   SetupOrProd:string,
   CapabilityID:string,
   ResourceGrpID:string,
   ResourceID:string,
   ConcurrentCapacity:number,
   DailyProdRate:number,
   NumResources:number,
   EstSetHours:number,
   EstProdHours:number,
   ProdStandard:number,
   StdFormat:string,
   StdBasis:string,
   OpsPerPart:number,
   ProdLabRate:number,
   SetupLabRate:number,
   ProdBurRate:number,
   SetupBurRate:number,
   ProdComplete:boolean,
   SetupComplete:boolean,
   ActProdHours:number,
   ActProdRwkHours:number,
   ActSetupHours:number,
   ActSetupRwkHours:number,
   SetupPctComplete:number,
   ActBurCost:number,
   ActLabCost:number,
   ReworkBurCost:number,
   ReworkLabCost:number,
   ResourceLock:boolean,
   SysCreateDate:string,
   SysCreateTime:number,
   OpDtlDesc:string,
   EstSetHoursPerMch:number,
   OverrideRates:boolean,
   ProdCrewSize:number,
   SetUpCrewSize:number,
   RemovedFromPlan:boolean,
   IsPrimaryProd:boolean,
   IsPrimarySetup:boolean,
   AutoSystemAdded:boolean,
   MobileAllocatedResource:boolean,
   SysRevID:number,
   SysRowID:string,
   QtyPerCycle:number,
   CapabilityDesc:string,
   OperOpStdID:string,
   PrimaryProd:boolean,
   PrimarySetup:boolean,
   ResourceGrpDesc:string,
   SchedResourceDesc:string,
   SchedResourceGrpDesc:string,
   SubContract:boolean,
   WISchedResourceDesc:string,
   WISchedResourceGrpDesc:string,
   ResourceDesc:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   CapabilityIDDescription:string,
   JobNumPartDescription:string,
   ResourceGrpIDDescription:string,
   ResourceIDDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperActionParamRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   ActionSeq:number,
   ActionParamSeq:number,
   ActionParamFieldDataType:string,
   ActionParamValueCharacter:string,
   ActionParamValueDate:string,
   ActionParamValueDecimal:number,
   ActionParamValueInteger:number,
   ActionParamValueLogical:boolean,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperActionRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   ActionSeq:number,
   ActionDesc:string,
   Required:boolean,
   Completed:boolean,
   CompletedBy:string,
   CompletedOn:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   EmpBasicName:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperAttchRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
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
   RowMod:string,
}

export interface Erp_Tablesets_JobOperInspRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   PlanSeq:number,
   InspPlanPartNum:string,
   InspPlanRevNum:string,
   SpecID:string,
   SpecRevNum:string,
   SysRevID:number,
   SysRowID:string,
   SpecHedDescription:string,
   BitFlag:number,
   InspPlanDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperMachParamRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   MachParamSeq:number,
   RequestCode:string,
   MachineNum:string,
   ToolNum:string,
   PartNum:string,
   ParamNum:number,
   ParamUpperLimit:number,
   ParamNominalValue:number,
   ParamLowerLimit:number,
   ParamDelayValue:number,
   SpecEnable:boolean,
   SpecControlAlarm:boolean,
   SpecRunAlarm:boolean,
   ProcSpecAlarm:boolean,
   ProcControlAlarm:boolean,
   PartQualSpecEnable:boolean,
   PartQualControlEnable:boolean,
   CreatedBy:string,
   CreatedOn:string,
   ChangedBy:string,
   ChangedOn:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperRestrictSubstRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   RestrictionTypeID:string,
   SubstanceID:string,
   Weight:number,
   WeightUOM:string,
   Manual:boolean,
   ExemptDate:string,
   ExemptCertificate:string,
   SysRevID:number,
   SysRowID:string,
   Exempt:boolean,
   OpCode:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   RestrictionDescription:string,
   SubstanceDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperRestrictionRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   RestrictionTypeID:string,
   OpCode:string,
   Manual:boolean,
   SysRevID:number,
   SysRowID:string,
   Weight:boolean,
   BitFlag:number,
   AssemblySeqDescription:string,
   JobNumPartDescription:string,
   RestrictionDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobOperRow{
   Company:string,
   JobComplete:boolean,
   OpComplete:boolean,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   OpCode:string,
   OpStdID:string,
   EstSetHours:number,
   EstProdHours:number,
   ProdStandard:number,
   StdFormat:string,
   StdBasis:string,
   OpsPerPart:number,
   QtyPer:number,
   QueStartDate:string,
   QueStartHour:number,
   StartDate:string,
   StartHour:number,
   DueDate:string,
   DueHour:number,
   MoveDueDate:string,
   MoveDueHour:number,
   ProdLabRate:number,
   SetupLabRate:number,
   ProdBurRate:number,
   SetupBurRate:number,
   AddedOper:boolean,
   Machines:number,
   SetUpCrewSize:number,
   ProdCrewSize:number,
   ProdComplete:boolean,
   SetupComplete:boolean,
   ActProdHours:number,
   ActProdRwkHours:number,
   ActSetupHours:number,
   ActSetupRwkHours:number,
   QtyCompleted:number,
   SetupPctComplete:number,
   EstScrap:number,
   EstScrapType:string,
   SubContract:boolean,
   IUM:string,
   EstUnitCost:number,
   DaysOut:number,
   PartNum:string,
   Description:string,
   VendorNum:number,
   PurPoint:string,
   CommentText:string,
   SchedRelation:string,
   RunQty:number,
   WIName:string,
   WIMachines:number,
   WIQueStartDate:string,
   WIQueStartHour:number,
   WIStartDate:string,
   WIStartHour:number,
   WIDueDate:string,
   WIDueHour:number,
   WIMoveDueDate:string,
   WIMoveDueHour:number,
   WIHoursPerMachine:number,
   WILoadDate:string,
   WILoadHour:number,
   ActBurCost:number,
   ActLabCost:number,
   ReworkBurCost:number,
   ReworkLabCost:number,
   MiscAmt:number,
   HoursPerMachine:number,
   LoadDate:string,
   LoadHour:number,
   ReloadNum:number,
   SndAlrtCmpl:boolean,
   RcvInspectionReq:boolean,
   JobEngineered:boolean,
   EstSetHoursPerMch:number,
   RevisionNum:string,
   AutoReceiptDate:string,
   LastLaborDate:string,
   CallNum:number,
   CallLine:number,
   LaborRate:number,
   BillableLaborRate:number,
   DocLaborRate:number,
   DocBillableLaborRate:number,
   Billable:boolean,
   UnitPrice:number,
   BillableUnitPrice:number,
   DocBillableUnitPrice:number,
   DocUnitPrice:number,
   LaborEntryMethod:string,
   PricePerCode:string,
   FAQty:number,
   QtyStagedToDate:number,
   RFQNeeded:boolean,
   RFQVendQuotes:number,
   RFQNum:number,
   RFQLine:number,
   RFQStat:string,
   SetupGroup:string,
   RestoreFlag:string,
   AnalysisCode:string,
   PrimarySetupOpDtl:number,
   PrimaryProdOpDtl:number,
   OpDesc:string,
   KitDate:string,
   GlbRFQ:boolean,
   BookedUnitCost:number,
   RecalcExpProdYld:boolean,
   UserMapData:string,
   RoughCutSched:boolean,
   SchedComment:string,
   Rpt1BillableLaborRate:number,
   Rpt2BillableLaborRate:number,
   Rpt3BillableLaborRate:number,
   Rpt1BillableUnitPrice:number,
   Rpt2BillableUnitPrice:number,
   Rpt3BillableUnitPrice:number,
   Rpt1LaborRate:number,
   Rpt2LaborRate:number,
   Rpt3LaborRate:number,
   Rpt1UnitPrice:number,
   Rpt2UnitPrice:number,
   Rpt3UnitPrice:number,
   SNRequiredOpr:boolean,
   SNRequiredSubConShip:boolean,
   Weight:number,
   WeightUOM:string,
   SendAheadType:string,
   SendAheadOffset:number,
   PrjRoleList:string,
   TearDwnEndDate:string,
   TearDwnEndHour:number,
   WITearDwnEndDate:string,
   WITearDwnEndHour:number,
   UseAllRoles:boolean,
   AssetPartNum:string,
   SerialNumber:string,
   ActualStartDate:string,
   ActualStartHour:number,
   ActualEndDate:string,
   ActualEndHour:number,
   FSJobStatus:number,
   Instructions:string,
   ProdUOM:string,
   GeneralPlanInfo:string,
   EstStdDescription:string,
   JDFOpCompleted:boolean,
   RemovedfromPlan:boolean,
   EstStdType:number,
   ExternalMES:boolean,
   PctReg:number,
   SetupMaterial:number,
   MaterialColorRating:number,
   MiscInfo1:string,
   MiscInfo2:string,
   SetupURL:string,
   ExpPctUp:number,
   ExpCycTm:number,
   ExpGood:number,
   NonProdLimit:number,
   AutoSpcEnable:boolean,
   AutoSpcPeriod:number,
   PartQualEnable:boolean,
   AutoSpcSubgroup:number,
   SysRevID:number,
   SysRowID:string,
   MobileOperation:boolean,
   ReWork:boolean,
   RequestMove:boolean,
   ContractID:string,
   PrinterID:string,
   LastPrintedDate:string,
   LastPCIDPrinted:string,
   CurrentPkgCode:string,
   ExternalMESSyncRequired:boolean,
   ExternalMESLastSync:string,
   QtyPerCycle:number,
   AttributeSetID:number,
   PlanningNumberOfPieces:number,
   StageNumber:string,
   TemplateID:string,
   ActScrapQty:number,
   AutoReceive:boolean,
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DisplayExtPrice:number,
   DisplayServAmt:number,
   DisplayServLaborRate:number,
   DisplayUnitPrice:number,
   DocDisplayExtPrice:number,
   DocDisplayServAmt:number,
   DocDisplayServLaborRate:number,
   DocDisplayUnitPrice:number,
   DspIUM:string,
   EnableAutoReceive:boolean,
   EnableSndAlrtCmpl:boolean,
   EnableSNReqSubConShip:boolean,
   EnableSNRequiredOpr:boolean,
   EstBurdenCost:number,
   EstLabHours:number,
   EstLaborCost:number,
   EstSubCost:number,
   FinalOpr:boolean,
   IsBaseCurrency:boolean,
   LaborEntryMethodDesc:string,
   LoadHrs:number,
   OpStdDescription:string,
   PrimaryProdOpDtlDesc:string,
   PrimaryResourceGrpDesc:string,
   PrimaryResourceGrpID:string,
   PrimarySetupOpDtlDesc:string,
   ProductionQty:number,
   RefreshResources:boolean,
   Rpt1DisplayExtPrice:number,
   Rpt1DisplayServAmt:number,
   Rpt1DisplayServLaborRate:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt2DisplayServAmt:number,
   Rpt2DisplayServLaborRate:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayExtPrice:number,
   Rpt3DisplayServAmt:number,
   Rpt3DisplayServLaborRate:number,
   Rpt3DisplayUnitPrice:number,
   ScrapQty:number,
   ShowStatusIcon:string,
   StdBasisDescription:string,
   StdFormatDescription:string,
   ActSubCost:number,
   EnableAttributeSetSearch:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   OpCodeOpDesc:string,
   PartNumAttrClassID:string,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackLots:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   RFQLineLineDesc:string,
   SetupGroupDescription:string,
   StageNoDescription:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumName:string,
   VendorNumCountry:string,
   VendorNumAddress2:string,
   VendorNumCurrencyCode:string,
   VendorNumZIP:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumAddress3:string,
   VendorNumCity:string,
   VendorNumVendorID:string,
   VendorPPZip:string,
   VendorPPCity:string,
   VendorPPAddress2:string,
   VendorPPPrimPCon:number,
   VendorPPAddress1:string,
   VendorPPCountry:string,
   VendorPPState:string,
   VendorPPName:string,
   VendorPPAddress3:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobPartRow{
   Company:string,
   JobNum:string,
   PartNum:string,
   RevisionNum:string,
   PartsPerOp:number,
   PartQty:number,
   StockQty:number,
   ShippedQty:number,
   ReceivedQty:number,
   WIPQty:number,
   QtyCompleted:number,
   ReservedQty:number,
   AllocatedQty900:number,
   PickingQty:number,
   PickedQty:number,
   LbrCostBase:number,
   MtlCostBase:number,
   JobClosed:boolean,
   JobComplete:boolean,
   Plant:string,
   PartDescription:string,
   IUM:string,
   ShipDocReq:boolean,
   ShipDocAvail:boolean,
   MtlList:string,
   PreventSugg:boolean,
   SysRevID:number,
   SysRowID:string,
   AttributeSetID:number,
   OrderQty:number,
   ProcessMode:string,
   EnableShipDocReq:boolean,
   PartmasterPart:boolean,
   EnableSugg:boolean,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartTrackInventoryByRevision:boolean,
   PartAttrClassID:string,
   PartPartDescription:string,
   PartTrackLots:boolean,
   PartIUM:string,
   PartSellingFactor:number,
   PartSalesUM:string,
   PartTrackInventoryAttributes:boolean,
   PartTrackSerialNum:boolean,
   RowMod:string,
}

export interface Erp_Tablesets_JobProdRow{
   Company:string,
   JobNum:string,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   ProdQty:number,
   WarehouseCode:string,
   TargetJobNum:string,
   TargetAssemblySeq:number,
   TargetMtlSeq:number,
   ShippedQty:number,
   ReceivedQty:number,
   WIPQty:number,
   CallNum:number,
   CallLine:number,
   TFLineNum:string,
   PartNum:string,
   Plant:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   DemandDtlSeq:number,
   DemandScheduleSeq:number,
   PlanUserID:string,
   PlanID:string,
   SysRevID:number,
   SysRowID:string,
   WIPToMiscShipment:boolean,
   RMANum:number,
   RMALine:number,
   RMAReceipt:number,
   RMADisp:number,
   DMRNum:number,
   DMRActionNum:number,
   AttributeSetID:number,
   PlanningNumberOfPieces:number,
   RevisionNum:string,
   CustID:string,
   CustName:string,
   DemandLinkSource:string,
   DemandLinkStatus:string,
   IUM:string,
   JHPartDesc:string,
   JHPartNum:string,
   MakeToJobQty:number,
   MakeToStockQty:number,
   MakeToType:string,
   MaxAllowedQty:number,
   MtlPartDesc:string,
   MtlPartNum:string,
   OrdWIPQty:number,
   OurStockQty:number,
   PullFromStockWarehouseCode:string,
   PullFromStockWarehouseDesc:string,
   ShipBy:string,
   SplitQty:number,
   StkWIPQty:number,
   TFOrdLine:number,
   TFOrdNum:string,
   TotalSplitQuantity:number,
   TrackSerialNumbers:boolean,
   Valid:boolean,
   AsmPartDesc:string,
   AsmPartNum:string,
   EnableAttributeSetSearch:boolean,
   DispNumberOfPieces:number,
   CustInactive:boolean,
   ShipToNumInactive:boolean,
   BitFlag:number,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartAttrClassID:string,
   PartTrackInventoryByRevision:boolean,
   PartSalesUM:string,
   PartTrackSerialNum:boolean,
   PartSellingFactor:number,
   PartTrackLots:boolean,
   PartIUM:string,
   PartTrackDimension:boolean,
   PartPricePerCode:string,
   PartPartDescription:string,
   PartTrackInventoryAttributes:boolean,
   WarehouseCodeDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobResourcesRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   OpDtlSeq:number,
   WhatIf:boolean,
   AllocNum:number,
   ResourceGrpID:string,
   ResourceID:string,
   ResourceDesc:string,
   CalendarName:string,
   SysRowID:string,
   RowMod:string,
}

export interface Erp_Tablesets_JobStageRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   StageSeq:number,
   StageNumber:string,
   SysRevID:number,
   SysRowID:string,
   BitFlag:number,
   StageNumberDescription:string,
   RowMod:string,
}

export interface Erp_Tablesets_OverrideSchedOrdersRow{
   Backwards:boolean,
   Company:string,
   DaysLate:number,
      /**  Job Number  */  
   JobNum:string,
   ReqDueDate:string,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
   SchedSeq:number,
      /**  Shows changed records for both cases: where SchedSeq was generated automatically or record was changed by user  */  
   IsChanged:boolean,
   StartDate:string,
      /**  Indicate which main job belong a group of jobs.  */  
   BatchJob:string,
      /**  Indicate which job is its parent.  */  
   ParentJob:string,
   MultiJobTopParent:boolean,
   MultiJobSchedSeq:number,
   SchedAsMultiJob:boolean,
   CurrentRow:boolean,
   IsDecimal:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OverrideSchedOrdersTableset{
   OverrideSchedOrders:Erp_Tablesets_OverrideSchedOrdersRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param companyID
      @param plantID
   */  
export interface GetCalculateGlobalSchedulingLastRun_input{
   companyID:string,
   plantID:string,
}

export interface GetCalculateGlobalSchedulingLastRun_output{
parameters : {
      /**  output parameters  */  
   multijobFlag:boolean,
}
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
      @param jobDs
      @param ds
   */  
export interface LoadOverrideSchedOrderViewList_input{
   jobDs:Erp_Tablesets_JobHeadListTableset[],
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface LoadOverrideSchedOrderViewList_output{
parameters : {
      /**  output parameters  */  
   jobDs:Erp_Tablesets_JobHeadListTableset,
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param jobDs
      @param ds
   */  
export interface LoadOverrideSchedOrderView_input{
   jobDs:Erp_Tablesets_JobEntryTableset[],
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface LoadOverrideSchedOrderView_output{
parameters : {
      /**  output parameters  */  
   jobDs:Erp_Tablesets_JobEntryTableset,
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface LoadOverrideSched_input{
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface LoadOverrideSched_output{
parameters : {
      /**  output parameters  */  
   WasChanged:boolean,
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface MultiJobUpdateSchedPri_input{
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface MultiJobUpdateSchedPri_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeBackwards_input{
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface OnChangeBackwards_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param multiJobSchedSeqOld
      @param currentJobNum
      @param ds
   */  
export interface OnChangeMultiJobSchedSeq_input{
   multiJobSchedSeqOld:number,
   currentJobNum:string,
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface OnChangeMultiJobSchedSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param proposedValue
      @param schedAsMultiJob
      @param multiJobTopParent
      @param jobNum
   */  
export interface OnChangingSchedSeq_input{
   proposedValue:number,
   schedAsMultiJob:boolean,
   multiJobTopParent:boolean,
   jobNum:string,
}

export interface OnChangingSchedSeq_output{
parameters : {
      /**  output parameters  */  
   askChangeSequenceOfSelectedJobOutsideOfItsGroup:boolean,
   isDecimal:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshOverrideSchedOrderView_input{
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface RefreshOverrideSchedOrderView_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

   /** Required : 
      @param multiJobSchedSeq
   */  
export interface SeqIsDecimal_input{
   multiJobSchedSeq:number,
}

export interface SeqIsDecimal_output{
parameters : {
      /**  output parameters  */  
   isDecimal:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateSchedPri_input{
   ds:Erp_Tablesets_OverrideSchedOrdersTableset[],
}

export interface UpdateSchedPri_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_OverrideSchedOrdersTableset,
}
}

