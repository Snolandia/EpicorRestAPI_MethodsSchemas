import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SchedulingBoardSvc
// Description: Provide data for the scheduling boards.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/$metadata", {
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
   Summary: Invoke method BuildJobLine
   Description: This methods will return all of the JobLine Header type records.  This will
be a JobLine record that would represent the JobHead and JobAsmbl.AssemblySeq = 0
information.  To retrieve the details run the ExpandJobLine publice method.
If ipJobNum and ipProjectID are both blank or unknown you will get all jobs for the current plant,
or if ipJobNum is not blank then just that job, or if ipjobnum is blank and
ipProjectID is not, then all jobs associated with that projectid.
   OperationID: BuildJobLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildJobLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildJobLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildJobLine(requestBody:BuildJobLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildJobLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/BuildJobLine", {
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
         resolve(data as BuildJobLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method BuildResourceLine
   Description: This methods will return all of the Resource Header type records.  This will
be a SchedulingBoard record that would represent the ResourceTimeUsed and it's assoc
information.
   OperationID: BuildResourceLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/BuildResourceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildResourceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BuildResourceLine(requestBody:BuildResourceLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<BuildResourceLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/BuildResourceLine", {
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
         resolve(data as BuildResourceLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateComment
   OperationID: UpdateComment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateComment(requestBody:UpdateComment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateComment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/UpdateComment", {
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
         resolve(data as UpdateComment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSchedulingRec
   Description: This methods will create new record of the SchedulingBoard.
   OperationID: GetNewSchedulingRec
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSchedulingRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSchedulingRec(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSchedulingRec_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/GetNewSchedulingRec", {
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
         resolve(data as GetNewSchedulingRec_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Restore
   Description: This method will restore the schedule based on the schedule id and return
and potential errors or warings with the restore in the SchedRestoreLog table.
   OperationID: Restore
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Restore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Restore_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Restore(requestBody:Restore_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Restore_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/Restore", {
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
         resolve(data as Restore_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReturnCalendarID
   Description: This methods will return the calendar id information along with whether or not
this calendar information can be used.
   OperationID: ReturnCalendarID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReturnCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReturnCalendarID(requestBody:ReturnCalendarID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReturnCalendarID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/ReturnCalendarID", {
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
         resolve(data as ReturnCalendarID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetLockSched
   Description: This method locks/unlocks the schedule of a specific jobnum.
   OperationID: SetLockSched
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetLockSched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetLockSched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetLockSched(requestBody:SetLockSched_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetLockSched_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/SetLockSched", {
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
         resolve(data as SetLockSched_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateAccess
   Description: Validate if the Use3rdPartySched is checked send a message that access is not allowed.
   OperationID: ValidateAccess
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAccess(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAccess_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SchedulingBoardSvc/ValidateAccess", {
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
         resolve(data as ValidateAccess_output)
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
      @param ds
   */  
export interface BuildJobLine_input{
   ds:Erp_Tablesets_SchedulingBoardTableset[],
}

export interface BuildJobLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SchedulingBoardTableset,
}
}

   /** Required : 
      @param ipResourceGrpID
      @param ipResourceID
      @param ipJobNum
      @param StartDate
      @param EndDate
   */  
export interface BuildResourceLine_input{
      /**  The resource group id to schedule for.  */  
   ipResourceGrpID:string,
      /**  The resource id or a list of resource id to schedule for  */  
   ipResourceID:string,
      /**  The job number to schedule for.  */  
   ipJobNum:string,
      /**  The StartDate to schedule for.  */  
   StartDate:string,
      /**  The EndDate to schedule for.  */  
   EndDate:string,
}

export interface BuildResourceLine_output{
   returnObj:Erp_Tablesets_SchedulingBoardTableset[],
}

export interface Erp_Tablesets_SchedRestoreLogRow{
      /**  The job number  */  
   JobNum:string,
      /**  The assembly sequence.  */  
   AssemblySeq:number,
      /**  The operation sequence.  */  
   OprSeq:number,
      /**  The description of the error or warning.  */  
   ErrorDesc:string,
      /**  The type, either E for Error or W for Warning.  */  
   ErrorType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SchedulingBoardJobMtlRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   PartNum:string,
   Description:string,
   QtyPer:number,
   RequiredQty:number,
   JobComplete:boolean,
   IssuedComplete:boolean,
   Plant:string,
   UnitPrice:number,
   DocUnitPrice:number,
   RevisionNum:string,
   BuyIt:boolean,
   Direct:boolean,
   RelatedOperation:number,
   IssuedQty:number,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.  
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
   Constrained:boolean,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   PORelNum:number,
      /**  Purchase order that this release record is related to.  */  
   PONum:number,
      /**  The line # of  PODetail record that the PORel record is related to.  */  
   POLine:number,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   DynAttrValueSetShortDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SchedulingBoardRow{
   BuildNum:number,
   RowNum:number,
   JobNum:string,
   AsmNum:number,
   OprNum:number,
   OpDtlNum:number,
   JobPartNum:string,
   AsmPartNum:string,
   OprPartNum:string,
   OpCode:string,
   ResourceGrpID:string,
   ResourceID:string,
   CapabilityID:string,
   BOMSequence:number,
   BOMLevel:number,
   JobPartDesc:string,
   AsmPartDesc:string,
   OprPartDesc:string,
   AsmRevisionNum:string,
   WIMode:string,
   WIStatus:string,
   WIName:string,
   NumMachines:number,
   TotalEstHours:number,
   TotalActHours:number,
   RemainHours:number,
   PrctCmplt:number,
   RemainPerMachHours:number,
      /**  The operation start date.  */  
   OSDate:string,
      /**  The operation start hour.  */  
   OSHour:number,
      /**  The operation due date.  */  
   ODDate:string,
      /**  The operation due hour.  */  
   ODHour:number,
      /**  The queue start date.  */  
   QSDate:string,
      /**  The queue start hour.  */  
   QSHour:number,
      /**  The queue days duration.  */  
   QDayDur:number,
      /**  The completed start date.  */  
   CSDate:string,
      /**  The completed start hour.  */  
   CSHour:number,
      /**  The completed days duration  */  
   CDayDur:number,
   WISDate:string,
      /**  The what if start hours.  */  
   WISHour:number,
      /**  The what if due date.  */  
   WIDDate:string,
      /**  The what if due hour.  */  
   WIDHour:number,
      /**  The move due date.  */  
   MDDate:string,
      /**  The move due hour.  */  
   MDHour:number,
      /**  The move days duration.  */  
   MDayDur:number,
      /**  On the critical path?  */  
   OnCritPath:boolean,
      /**  Is operation a subcontract?  */  
   OprSubcontract:boolean,
   Parent:number,
   PriorPeer:number,
   NextPeer:number,
      /**  The last operation of the parent assembly.  */  
   LastOper:boolean,
   Company:string,
      /**  Indicates that the assembly has operations.  Always true for operations.  */  
   HasOper:boolean,
      /**  Indicates that the asm should show children.  */  
   ShowChildrenFlag:boolean,
      /**  Indicates that the record should be shown.  */  
   OnScreenFlag:boolean,
      /**  On Asm = 0 this set to 'E' for Engineered, 'R' for Released.  */  
   JobStatus:string,
   JobLateStatus:string,
      /**  The estimated duration hours.  */  
   EstDurHours:number,
   Lateness:number,
   BuildAsms:boolean,
      /**  Has the operation started?  */  
   OperationStarted:boolean,
   Plant:string,
   SetupGroup:string,
   PrimarySetupOpDtl:number,
   PrimaryProdOpDtl:number,
   SchedResourceGrpID:string,
   SchedResourceID:string,
   WISchedResourceGrpID:string,
   WISchedResourceID:string,
   ConstraintNoMtl:boolean,
   ConstraintNoPO:boolean,
   ConstraintCapacity:boolean,
   OpComplete:boolean,
   SchedLocked:boolean,
   ResourceIDDesc:string,
   ResourceGrpIDDesc:string,
   CapabilityIDDesc:string,
      /**  Sort by Start Date.  */  
   SortStartDate:string,
      /**  Sort by Job.  */  
   SortJob:string,
      /**  Sort by Part.  */  
   SortPart:string,
      /**  Sort by Cust ID.  */  
   SortCustID:string,
      /**  Sort by Due Date.  */  
   SortDueDate:string,
      /**  Sort by Days Late.  */  
   SortDaysLate:string,
      /**  Sort by Setup Group  */  
   SortSetupGroup:string,
      /**  Sort by OpCode.  */  
   SortOpCode:string,
      /**  The calculated custid.  */  
   CalcCustID:string,
      /**  The job production quantity.  */  
   ProdQty:number,
      /**  The jobhead quantity completed.  */  
   JobHeadQtyCompleted:number,
      /**  The job type.  */  
   JobType:string,
      /**  The joboper quantity completed  */  
   JobOperQtyCompleted:number,
      /**  The run quantity from the joboper table.  */  
   RunQty:number,
      /**  The jobhead start date.  */  
   StartDate:string,
      /**  The jobhead required due date.  */  
   ReqDueDate:string,
      /**  The revision number for the part on the jobhead record.  */  
   JobRevisionNum:string,
      /**  Is the job locked because winame is not equal the dcduserid?  */  
   JobLocked:boolean,
      /**  The allocation number from the resourcetimeused table for resource boards.  Will be zero for job boards.  */  
   AllocNum:number,
      /**  The operation description  */  
   OpDesc:string,
      /**  Is this a batch operation?  */  
   Batch:boolean,
      /**  Operation start time.  */  
   OprStartTime:string,
      /**  Operation end time.  */  
   OprEndTime:string,
      /**  The parent operation rowid  */  
   OperRowIdent:string,
   SetupGrpDescription:string,
   PartPlantNonStock:boolean,
   PartPlantMaxMfgLotSize:number,
      /**  The number of days late.  */  
   DaysLate:number,
   Machines:number,
   ProductionComplete:boolean,
   SetupComplete:boolean,
   SchedComment:string,
      /**  What-If Resource Description.  */  
   WISchedResourceIDDesc:string,
      /**  Current Resource Description.  */  
   SchedResourceIDDesc:string,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   IgnoreMtlConstraints:boolean,
   ResourceTotalEstHours:number,
   ProductionYield:boolean,
      /**  ID of related Attribute Class  */  
   AsmAttrClassID:string,
      /**  Description of values in set  */  
   AsmAttrDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AsmAttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   AsmShortDesc:string,
      /**  ID of related Attribute Class  */  
   JobAttrClassID:string,
      /**  Description of values in set  */  
   JobAttrDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   JobAttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   JobShortDesc:string,
      /**  ID of related Attribute Class  */  
   OprAttrClassID:string,
      /**  Description of values in set  */  
   OprAttrDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   OprAttributeSetID:number,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   OprShortDesc:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   OprRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SchedulingBoardTableset{
   SchedulingBoard:Erp_Tablesets_SchedulingBoardRow[],
   SchedRestoreLog:Erp_Tablesets_SchedRestoreLogRow[],
   SchedulingBoardJobMtl:Erp_Tablesets_SchedulingBoardJobMtlRow[],
   SchedulingJob:Erp_Tablesets_SchedulingJobRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SchedulingJobRow{
   Company:string,
   JobNum:string,
   ProjectID:string,
   Plant:string,
   ExpandJob:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface GetNewSchedulingRec_output{
   returnObj:Erp_Tablesets_SchedulingBoardTableset[],
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
      @param ipScheduleID
   */  
export interface Restore_input{
      /**  The Schedule ID  */  
   ipScheduleID:number,
}

export interface Restore_output{
   returnObj:Erp_Tablesets_SchedulingBoardTableset[],
parameters : {
      /**  output parameters  */  
   opJobList:string,
}
}

   /** Required : 
      @param ipResourceGrpID
      @param ipResourceID
   */  
export interface ReturnCalendarID_input{
      /**  The resource group id locate calendar for.  */  
   ipResourceGrpID:string,
      /**  The resource id or a list of resource id locate calendar for.  */  
   ipResourceID:string,
}

export interface ReturnCalendarID_output{
parameters : {
      /**  output parameters  */  
   opCalendarID:string,
   opValidCalendar:boolean,
}
}

   /** Required : 
      @param inLockedStatus
      @param ds
   */  
export interface SetLockSched_input{
      /**  The locked status of the schedule.  */  
   inLockedStatus:boolean,
   ds:Erp_Tablesets_SchedulingBoardTableset[],
}

export interface SetLockSched_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SchedulingBoardTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateComment_input{
   ds:Erp_Tablesets_SchedulingBoardTableset[],
}

export interface UpdateComment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SchedulingBoardTableset,
}
}

export interface ValidateAccess_output{
      /**  bool: access is allowed or not  */  
   returnObj:boolean,
}

