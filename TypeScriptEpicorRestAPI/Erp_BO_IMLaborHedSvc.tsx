import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.IMLaborHedSvc
// Description: Business Object to handle: Add, Update and Delete of LaborHed, LaborDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/$metadata", {
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
   Summary: Invoke method AddIndirectLabor
   Description: Add LaborHed and LaborHed related tables
   OperationID: AddIndirectLabor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddIndirectLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddIndirectLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddIndirectLabor(requestBody:AddIndirectLabor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddIndirectLabor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/AddIndirectLabor", {
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
         resolve(data as AddIndirectLabor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteIndirectLabor
   Description: Delete LaborHed and LaborHed related tables
   OperationID: DeleteIndirectLabor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteIndirectLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteIndirectLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteIndirectLabor(requestBody:DeleteIndirectLabor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteIndirectLabor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/DeleteIndirectLabor", {
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
         resolve(data as DeleteIndirectLabor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateIndirectLabor
   Description: Update LaborHed and LaborHed related tables
   OperationID: UpdateIndirectLabor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateIndirectLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIndirectLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateIndirectLabor(requestBody:UpdateIndirectLabor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateIndirectLabor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/UpdateIndirectLabor", {
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
         resolve(data as UpdateIndirectLabor_output)
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
      @param IMLaborHedTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddIndirectLabor_input{
   IMLaborHedTableset:Erp_Tablesets_IMLaborHedTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddIndirectLabor_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset,
}
}

   /** Required : 
      @param IMLaborHedTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface DeleteIndirectLabor_input{
   IMLaborHedTableset:Erp_Tablesets_IMLaborHedTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface DeleteIndirectLabor_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

export interface Erp_Tablesets_IMIntegrationKeyRow{
      /**  The master file which the integration is related to.  */  
   TableName:string,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMIntegrationKeyTableset{
   IMIntegrationKey:Erp_Tablesets_IMIntegrationKeyRow[],
   IMNaturalKeys:Erp_Tablesets_IMNaturalKeysRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMLaborDtlCommentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier of the Labor Header the comment relates to.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  */  
   CommentNum:number,
      /**   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  */  
   CommentType:string,
      /**  The comment text.  */  
   CommentText:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  */  
   TaskSeqNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Key for related IntQueInOut  */  
   IntQueID:number,
      /**  Unique identifier of related integration record. The value is a GUID  */  
   ExternalKey:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMLaborDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborType:string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborTypePseudo:string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   ReWork:boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   ReworkReasonCode:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   JCDept:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   OpCode:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   LaborHrs:number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   BurdenHrs:number,
      /**  The Total production quantity reported.  */  
   LaborQty:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   ScrapReasonCode:string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   SetupPctComplete:number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   Complete:boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   IndirectCode:string,
      /**  A short note that the user can make about the labor transaction.  */  
   LaborNote:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   ExpenseCode:string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   AppliedToSchedule:boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   ClockInMInute:number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   ClockOutMinute:number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   ClockInDate:string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   ClockinTime:number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   ClockOutTime:number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   ActiveTrans:boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   OverRidePayRate:number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   LaborRate:number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   BurdenRate:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   OpComplete:boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   EarnedHrs:number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   AddedOper:boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   PayrollDate:string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   GLTrans:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   InspectionPending:boolean,
      /**  The service call that this service record belongs to.  */  
   CallNum:number,
      /**  The line number of the service call this labor detail is for.  */  
   CallLine:number,
      /**  the service that is being performed on this line.  */  
   ServNum:number,
      /**  A unique code that identifies the Service  */  
   ServCode:string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   WipPosted:boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   DiscrpRsnCode:string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   ParentLaborDtlSeq:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   LaborEntryMethod:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   BFLaborReq:boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   ABTUID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   PBInvNum:number,
      /**  The payment method of the time.  */  
   PMUID:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  The date the time received final approval.  */  
   ApprovedDate:string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   QuickEntryCode:string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   TimeStatus:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   CreatedViaTEWeekView:boolean,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  The User ID of the submitter.  */  
   SubmittedBy:string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   PBRateFrom:string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   PBCurrencyCode:string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   PBHours:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   DocPBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt1PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt2PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt3PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   DocPBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt1PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt2PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt3PBChargeAmt:number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  Links to PActDtl.ActID  */  
   ActID:number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   DtailID:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used By Project Analysis Process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process.  */  
   AsOfSeq:number,
      /**  JDFInputFiles  */  
   JDFInputFiles:string,
      /**  JDFNumberOfPages  */  
   JDFNumberOfPages:string,
      /**  BatchWasSaved  */  
   BatchWasSaved:string,
      /**  AssignToBatch  */  
   AssignToBatch:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchRequestMove  */  
   BatchRequestMove:boolean,
      /**  BatchPrint  */  
   BatchPrint:boolean,
      /**  BatchLaborHrs  */  
   BatchLaborHrs:number,
      /**  BatchPctOfTotHrs  */  
   BatchPctOfTotHrs:number,
      /**  BatchQty  */  
   BatchQty:number,
      /**  BatchTotalExpectedHrs  */  
   BatchTotalExpectedHrs:number,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Downtime  */  
   Downtime:boolean,
      /**  RefJobNum  */  
   RefJobNum:string,
      /**  RefAssemblySeq  */  
   RefAssemblySeq:number,
      /**  RefOprSeq  */  
   RefOprSeq:number,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   TimeAutoSubmit:boolean,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  BillServiceRate  */  
   BillServiceRate:number,
      /**  Pay Hours used for HCM  */  
   HCMPayHours:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
      /**  Used by Epicor FSA  */  
   CallCode:string,
      /**  Used by Epicor FSA  */  
   ContractCode:string,
      /**  Used by Epicor FSA  */  
   WarrantyCode:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Field Service Contract Num  */  
   ContractNum:number,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMLaborHedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  */  
   EmployeeNum:string,
      /**  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  */  
   LaborHedSeq:number,
      /**   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  */  
   PayrollDate:string,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  */  
   ClockInDate:string,
      /**  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  */  
   ClockInTime:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  */  
   ActualClockInTime:number,
      /**  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  */  
   ActualClockinDate:string,
      /**   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  */  
   LunchStatus:string,
      /**   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  */  
   ActLunchOutTime:number,
      /**   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  */  
   LunchOutTime:number,
      /**   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  */  
   ActLunchInTime:number,
      /**   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  */  
   LunchInTime:number,
      /**  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  */  
   ClockOutTime:number,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  */  
   ActualClockOutTime:number,
      /**   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  */  
   PayHours:number,
      /**  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  */  
   FeedPayroll:boolean,
      /**  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  */  
   TransferredToPayroll:boolean,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  */  
   TranSet:string,
      /**   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  */  
   ActiveTrans:boolean,
      /**   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  */  
   ChkLink:string,
      /**  BatchTotalHrsDisp  */  
   BatchTotalHrsDisp:string,
      /**  BatchHrsRemainDisp  */  
   BatchHrsRemainDisp:string,
      /**  BatchHrsRemainPctDisp  */  
   BatchHrsRemainPctDisp:string,
      /**  BatchSplitHrsMethod  */  
   BatchSplitHrsMethod:string,
      /**  BatchAssignTo  */  
   BatchAssignTo:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchStartHrs  */  
   BatchStartHrs:string,
      /**  BatchEndHrs  */  
   BatchEndHrs:string,
      /**  BatchTotalHrs  */  
   BatchTotalHrs:number,
      /**  BatchHrsRemain  */  
   BatchHrsRemain:number,
      /**  BatchHrsRemainPct  */  
   BatchHrsRemainPct:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Key from related IntQueInOut  */  
   IntQueID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMLaborHedTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMLaborDtl:Erp_Tablesets_IMLaborDtlRow[],
   IMLaborHed:Erp_Tablesets_IMLaborHedRow[],
   IMLaborDtlComment:Erp_Tablesets_IMLaborDtlCommentRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMNaturalKeysRow{
   KeyValue:string,
   KeyColumn:string,
   Sequence:number,
   PrimaryKey:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntQueInOutRow{
      /**  The unique key from IntQueIn or IntQueOut  */  
   IntQueID:number,
      /**  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  */  
   Action:string,
      /**  "I" for incoming or "O" for outgoing  */  
   IncomingOutgoing:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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
      @param IMLaborHedTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface UpdateIndirectLabor_input{
   IMLaborHedTableset:Erp_Tablesets_IMLaborHedTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface UpdateIndirectLabor_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

