import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.JobClosingSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/$metadata", {
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
   Summary: Invoke method AllowCloseJob
   Description: This method exists soley for the purpose of allowing security for
availability of the close job field to be defined.
   OperationID: AllowCloseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AllowCloseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AllowCloseJob(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/AllowCloseJob", {
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
   Summary: Invoke method CloseJob
   Description: Call this method to close or complete the job.  The Job database is not updated
till this method is successfully executed.
   OperationID: CloseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/CloseJob", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnableSerialMatching
   Description: Call this method when it is necessary to know in UI if the Serial Matching option should be enabled.
   OperationID: EnableSerialMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableSerialMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSerialMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableSerialMatching(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/EnableSerialMatching", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobClosing
   Description: Returns a new , empty Call JobClosingDataSet row.
   OperationID: GetNewJobClosing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobClosing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobClosing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobClosing(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/GetNewJobClosing", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobClosingList
   Description: This method creates a new JobClosingListDataSet row entry.
   OperationID: GetNewJobClosingList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobClosingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobClosingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobClosingList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/GetNewJobClosingList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobClosed
   Description: Call this method when the value of Epicor.Mfg.BO.JobClosingDataSet.JobClosed changes.
   OperationID: OnChangeJobClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobClosed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/OnChangeJobClosed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobCompletion
   Description: Call this method when the value of Epicor.Mfg.BO.JobClosingDataSet.JobComplete changes.
   OperationID: OnChangeJobCompletion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobCompletion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobCompletion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobCompletion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/OnChangeJobCompletion", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method when the user selects a job.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/OnChangeJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreCloseJob
   Description: This method will return a record in the LegalNumberGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCloseJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCloseJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCloseJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCloseJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/PreCloseJob", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectMultipleJob
   Description: Call this method when the user selects multiple jobs.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: SelectMultipleJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectMultipleJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectMultipleJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectMultipleJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/SelectMultipleJob", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectJobByJobNum
   Description: Call this method when the user selects multiple jobs.  This method populates
the Epicor.Mfg.BO.JobClosingDataSet dataset with Job , JobOper and JobMtl information.
   OperationID: SelectJobByJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectJobByJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectJobByJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectJobByJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobClosingSvc/SelectJobByJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface AllowCloseJob_output{
}

   /** Required : 
      @param ds
   */  
export interface CloseJob_input{
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface CloseJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface EnableSerialMatching_input{
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface EnableSerialMatching_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
   plEnable:boolean,
}
}

export interface Erp_Tablesets_JobClosingListRow{
      /**  Company identifier  */  
   Company:string,
   JobNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobClosingListTableset{
   JobClosingList:Erp_Tablesets_JobClosingListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobClosingRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
   PrintProductionDetail:boolean,
   BackFlush:boolean,
   StockQty:number,
   OrderQty:number,
   ReceivedToStockQty:number,
   ShippedQty:number,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
   CompleteQty:number,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
   CanPrintProfitInfo:boolean,
      /**  If this field value is yes and backflush check box is yes then perform backflush processing in the backend.  */  
   BackFlushProcessing:boolean,
   LegalNumber:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
   UserAllowedToCloseJob:boolean,
      /**  Yes means the Job uses work centers from multiple plants.  */  
   MultiplePlant:boolean,
      /**  User response to job uses Multiple plant  */  
   MultiplePlantContinue:number,
   PendingInspection:boolean,
   PendingInspectionContinue:number,
   QuantityContinue:number,
   LegalNumberMessage:string,
   JobUOM:string,
   BitFlag:number,
   OpenDMR:boolean,
   OpenDMRContinue:boolean,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag to indicate whether WIPCleared column should be enabled  */  
   EnableWIPCleared:boolean,
   ReceivedToJobQty:number,
   PartNumSalesUM:string,
   PartNumSellingFactor:number,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobClosingTableset{
   JobClosing:Erp_Tablesets_JobClosingRow[],
   JobMtl:Erp_Tablesets_JobMtlRow[],
   JobOper:Erp_Tablesets_JobOperRow[],
   JobPart:Erp_Tablesets_JobPartRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   JobComplete:boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   PartNum:string,
      /**  A description of the material.  */  
   Description:string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   QtyPer:number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   IUM:string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  The material burden rate for this Job Material.  */  
   MtlBurRate:number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstMtlBurUnitCost:number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   IssuedQty:number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   TotalCost:number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   MtlBurCost:number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   ReqDate:string,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  The salvage material burden rate for this Job Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   SalvageQtyToDate:number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   SalvageCredit:number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   SalvageMtlBurCredit:number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   BuyIt:boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   Ordered:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   PurComment:string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   BackFlush:boolean,
      /**  Estimated Scrap.  */  
   EstScrap:number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   Direct:boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   MaterialMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialSubCost:number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialBurCost:number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageMtlCredit:number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageLbrCredit:number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageBurCredit:number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageSubCredit:number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  The service call that this Material belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this material relates to.  */  
   CallLine:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  FS - Unit Price for the Material in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  Is this a billable material item.  */  
   Billable:boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   ShippedQty:number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   DocUnitPrice:number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   QtyStagedToDate:number,
      /**  This material was added after initial setup of the job  */  
   AddedMtl:boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   SCMiscCode:string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   WIReqDate:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   BaseRequiredQty:number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   BaseUOM:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstMtlUnitCredit:number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstLbrUnitCredit:number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstBurUnitCredit:number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstSubUnitCredit:number,
      /**  The material quantity that has been loaned out to another job.  */  
   LoanedQty:number,
      /**  The material quantity that has been borrowed from another job.  */  
   BorrowedQty:number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   ReassignSNAsm:boolean,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  IsPOCostingMaintained  */  
   IsPOCostingMaintained:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  POCostingFactor  */  
   POCostingFactor:number,
      /**  PlannedQtyPerUnit  */  
   PlannedQtyPerUnit:number,
      /**  POCostingDirection  */  
   POCostingDirection:number,
      /**  POCostingUnitVal  */  
   POCostingUnitVal:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  ShowStatusIcon  */  
   ShowStatusIcon:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   StagingLotNum:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  The identification of related StageNo.  */  
   RelatedStage:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
      /**  Indicates if the job material should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the job material is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  The currency switch flag  */  
   CurrencySwitch:boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**  The display of extended price.  */  
   DisplayExtPrice:number,
      /**  The display unit price.  */  
   DisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  The document display extended price  */  
   DocDisplayUnitPrice:number,
      /**  BuyIt field for display in the UI.  */  
   dspBuyIt:boolean,
      /**  Display IUM (readonly)  */  
   DspIUM:string,
      /**  Should the backflush field be enabled?  */  
   EnableBackflush:boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   EnableBuyIt:boolean,
      /**  flag to determine whether the Configure Option should be enabled.  */  
   EnableConfigure:boolean,
      /**  flag to determine whether the Make Direct field should be enabled.  */  
   EnableDirect:boolean,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   EnableFixedQty:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   EnableRcvInspReq:boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableSplitCosts:boolean,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   EstCost:number,
      /**  The name of the calling program  */  
   IPCaller:string,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
   IsMtlConfigurationOn:boolean,
   IsMtlConfigureOn:boolean,
   IsMtlExtConfig:boolean,
      /**  IsMtlRevisionApproved  */  
   IsMtlRevisionApproved:boolean,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   PartExists:boolean,
      /**  Calculated field gets list of available Sites  */  
   PlantList:string,
      /**  Price Per Code Description  */  
   PricePerCodeDescription:string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  The description of the related operation  */  
   RelatedOperationDesc:string,
      /**  Logical used to determine if record is created from PO Entry.  */  
   RetainValues:boolean,
   Rpt1DisplayExtPrice:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayExtPrice:number,
   Rpt3DisplayUnitPrice:number,
      /**  BaseUOM for SalvagePartNum  */  
   SalvageBaseUOM:string,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   ShowInspRqdImg:boolean,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   SubContract:boolean,
      /**  Can the backflush be unchecked?  */  
   AllowBackflushUncheck:boolean,
   EnableAttributeSetSearch:boolean,
   EnableSalvageAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts  */  
   PlanningNumberOfPiecesDisp:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   SalvagePlanningNumberOfPiecesDisp:number,
      /**  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  */  
   SkipUnitPriceCalc:boolean,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this job material is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
      /**  Indicates this row is selected for action.  */  
   SelectedForAction:boolean,
      /**  The allocated quantity for this job material.  */  
   AllocatedQty:number,
      /**  The reserved quantity for this job material.  */  
   ReservedQty:number,
      /**  The available quantity for this job material.  */  
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobOperRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobOper records are also marked.  This is used to make database access to open operation records more efficient.  */  
   JobComplete:boolean,
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
      /**  Operation Master Code - Links the JobOper  record with a OpMaster record.  Default is given from WrkCenter.OpCode.  Must be valid in the OpMaster file.  */  
   OpCode:string,
      /**   The Operation standard ID.  This links the JobOper to the OpStd master file.  This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  */  
   OpStdID:string,
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
      /**  Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   QueStartDate:string,
      /**  Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   QueStartHour:number,
      /**  Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   StartHour:number,
      /**  Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   DueHour:number,
      /**  Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   MoveDueDate:string,
      /**  Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   MoveDueHour:number,
      /**  Labor rate used for estimated production labor costs. Default from the OpMaster.ProdLabRate.  */  
   ProdLabRate:number,
      /**  Labor rate for estimated setup labor costs. Default from the OpMaster.SetupLabRate.  */  
   SetupLabRate:number,
      /**  The burden rate to be used for the production time on this operation. (EstProdHrs X ProdBurRate). Default from the WrkCenter.ProdBurRate.  */  
   ProdBurRate:number,
      /**  The burden rate to be used for the Setup time on this operation. (EstSetHours X ProdBurRate). Default from the WrkCenter.SetupBurRate.  */  
   SetupBurRate:number,
      /**  This indicates if this is an "added operation". An added operation is one that was not planned on.  */  
   AddedOper:boolean,
      /**  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  */  
   Machines:number,
      /**  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to setup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  */  
   SetUpCrewSize:number,
      /**  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  */  
   ProdCrewSize:number,
      /**  A flag indicating if the production is complete for this operation. It is updated via Labor Entry.  */  
   ProdComplete:boolean,
      /**  Flag that indicates if Setup is complete on this operation. This flag is only used when the operation has EstSetupHours > 0.00.  */  
   SetupComplete:boolean,
      /**  Total Actual Production Hours. A summary of non-setup LaborDtl.BurdenHrs. This includes REWORK hours.  This is maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActReworkHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H").  */  
   ActProdHours:number,
      /**  Total Actual Production Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "P" and Rework = Yes. This number is also included as part of the JobOPer.ActProdHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActProdHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActProdRwkHours:number,
      /**  Actual setup hours.  A summary of setup (LaborDtl.LaborType = S) labor transactions hours (LaborDtl.Burden). Actual Setup hours reduce the shop load if the system is configured to remove load based on hours (JCSyst.RemoveLoad = "H").  */  
   ActSetupHours:number,
      /**  Total Actual Setup Rework  Hours. A summary of rework labor transactions (LaborDtl.BurdenHrs) where LaborDtl.LaborType = "S" and Rework = Yes. This number is also included as part of the JobOPer.ActSetupHours.  Maintained via write/delete triggers on the LaborDtl file. Along with JobOper.ActSetHours it is used to reduce the shop load if the system is configured to remove load by actual hours (JCSyst.RemoveLoad = "H"). (See the lib/inopload.i code for load remaining logic)  */  
   ActSetupRwkHours:number,
      /**   For Non Subcontract operations: A summary of labor transaction detail. (LaborDtl.LaborQty). Labor entry/collection maintains this field.  Only the LaborQty for transactions that are Production labor ( LaborType = P ) and Not rework (LaborDtl.Rework = No) are included in this summary.
This quantity is used to reduce shop load when the system is configured to reduce load based on quantity completed. (JCSyst.RemoveLoad = Q)
For Subcontract Operations this field is updated by the Purchased Receipt process. The detail records are in the PartTran file.  */  
   QtyCompleted:number,
      /**  Setup function percent complete.  Maintained via labor entry.  */  
   SetupPctComplete:number,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
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
      /**  The PartNum to be shipped to the subcontract. Default the JobHead.PartNum or JobAsmbl.PartNum depending on the JobMtl.AssemblySeq.  */  
   PartNum:string,
      /**  Description used only for subcontract operations  */  
   Description:string,
      /**  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  */  
   VendorNum:number,
      /**  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Editor widget for Job operation comments.  */  
   CommentText:string,
      /**   Indicates the scheduling relationship between this and the preceding  operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  */  
   SchedRelation:string,
      /**   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  */  
   RunQty:number,
      /**   This field is blank or contains the UserID. When not blank it indicates that the operations schedule has been changed and is considered as being in a "What If" mode.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  This is the What-If number of machines that this operation will run on at the same time.  Setup by and for scheduling from the Machines field.  */  
   WIMachines:number,
      /**  What-if Scheduled queue start date. Not directly maintainable, updated via the scheduling process.  */  
   WIQueStartDate:string,
      /**  What-if Scheduled queue start hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIQueStartHour:number,
      /**  What if Scheduled production start date. Not directly maintainable, updated via the scheduling process.  */  
   WIStartDate:string,
      /**  This field is established by scheduling. It represents the What If "Hour offset from the beginning of the work day" when this operation is scheduled to begin.  */  
   WIStartHour:number,
      /**  What If Scheduled production due date. Not directly maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling. It represents the "Hour offset from the beginning of the work day" when this operation is scheduled to end.  */  
   WIDueHour:number,
      /**  What-If Scheduled move due date. Not directly maintainable, updated via the scheduling process.  */  
   WIMoveDueDate:string,
      /**  What-if Scheduled move due hour offset from the beginning of the work day.  This field is established by scheduling.  */  
   WIMoveDueHour:number,
      /**  The Number of Hours per machine per day that this operations "What If" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining ShopLoad records.  */  
   WIHoursPerMachine:number,
      /**  Date at which the operations current outstanding "What-If" load starts at.  Updated by the JobOper write trigger. (See LoadDate)  */  
   WILoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding "What-If"  load. Related to WILoadDate.  */  
   WILoadHour:number,
      /**  Total Burden cost to date. This is update via the LaborDtl\Write.p trigger procedure. It includes ALL burden costs (Setup, Production and Rework)  */  
   ActBurCost:number,
      /**   FOR NON-SUBCONTRACT OPERATIONS: Total of "ALL" labor costs to date. This includes Setup, Production and Rework. Updated via the LaborDtl.Write.p trigger.
FOR SUBCONTRACT OPERATIONS: The Total Cost, updated via the receipt process.  */  
   ActLabCost:number,
      /**  Total Rework Burden cost todate. This value is also included in the ActBurCost total. It includes both setup & production rework. Updated via LaborDtl\Write.P trigger.  */  
   ReworkBurCost:number,
      /**  Total Rework Labor cost to date. This value is also included in the ActLabCost field. This includes both Setup & Production. Updated via the LaborDtl\Write.p trigger.  */  
   ReworkLabCost:number,
      /**   A total additional charge that is incurred when purchasing this service. Ex(Lot,Setup,Handling,etc...).
Defaulted from VendPart.MiscAmt. This is NOT part of the a Unit Cost. It is NOT consider in the logic of using Minimum Cost.  */  
   MiscAmt:number,
      /**  The Number of Hours per machine per day that this operations "actual" schedule is based on.  This is for "Inbetween" days, not first or last days.  It is a copy of WrkCenter.HoursPerMachine field at the time of scheduling.  Used in logic of maintaining the ShopLoad records.  */  
   HoursPerMachine:number,
      /**   Date at which the operations current outstanding load starts at.
Ex: Op schedule is 2/1/97 - 2/10/97, initially LoadDate = 2/1/97. As load is relieved through labor processing the LoadDate moves forward accordingly. When 1/2 completed the LoadDate would be 2/5/97. This field is primarily used by the Scheduling Board to calculate the graphical image of outstanding load.  Updated by the JobOper write trigger.  */  
   LoadDate:string,
      /**  "Hour offset from the beginning of the work day" for the operations outstanding load. Related to LoadDate.  */  
   LoadHour:number,
      /**  Internally used field to prevent redundant read of JobOper during execution of "Reloader" program. (See WrkCenter.ReloadNum)  */  
   ReloadNum:number,
      /**  Controls if an alert is to be sent when this JobOper is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if  Inspection is required when items are received to this JobOper (subcontract only). Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Identical to JobHead.JobEngineered.  ShopLoad capacity is only allocated to Jobs where JobEngineered = YES.  */  
   JobEngineered:boolean,
      /**   The estimated set up hours per machine.
Default from OpStd.SetupHours.  Used to calculate JobOper.EstSetupHours.  */  
   EstSetHoursPerMch:number,
      /**   Part Revision number.
Pertains to subcontracting operations only.   An optional field.   Related JobAsmbl.RevisionNum is used as the default.  */  
   RevisionNum:string,
      /**  Currently not used. Prep for future development.  */  
   AutoReceiptDate:string,
      /**  The labor date of the last labor transaction that was posted to this operation.  Used by the JobOper write trigger Auto Receieve logic.  */  
   LastLaborDate:string,
      /**  The service call that this operation belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this operation relates to.  */  
   CallLine:number,
      /**  Labor rate used for  time on an operation.  Time per hour per technician. in base currency.  */  
   LaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. in base currency. This field considers the percentage coverage of a warranty or contract.  */  
   BillableLaborRate:number,
      /**  Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. Does not consider warranty or contract  */  
   DocLaborRate:number,
      /**  Billable Labor rate used for  time on a service.  Time per hour per technician. In Customer currency. considers warranty or contract  */  
   DocBillableLaborRate:number,
      /**  FS - Is this a billable operation.  */  
   Billable:boolean,
      /**  FS - Unit Price for the subcontract in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the subcontract in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the subcontract in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  FS - Unit Price for the for the Subcontract in Customer currency.  */  
   DocUnitPrice:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated), "B" - Backflush or "X" - Time - Backflush Qty.  */  
   LaborEntryMethod:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  The quantity requested for first article inspection.  */  
   FAQty:number,
      /**  The "to date" quantity that has been moved to the input Warehouse/Bin of the subsequent operations ResourceGroup/Resource input Warehouse/Bin.  This is NOT A balance.  It is a "to date" value.  It is not reduced as it is consumed.  Used in calculation of "Outstanding" WIP in the Request Material/WIP program (ame30-dg.w).  Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the WIP material in/out of the staging area (Issues, Returns).  */  
   QtyStagedToDate:number,
      /**  A flag to indicate that this job operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job subcontract operation.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Used to group operation to save on setups.  */  
   SetupGroup:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**   Identifies the primary JobOpDtl to be used for setup.  The setup time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = S or B.  */  
   PrimarySetupOpDtl:number,
      /**   Identifies the primary JobOpDtl to be used for production.  The production run time for the operation is determined on the JobOpDtl.
If <> 0, must identify a valid JobOpDtl.  The JobOpDtl needs to have a RequiredFor = P or B.  */  
   PrimaryProdOpDtl:number,
      /**  Operation Description.  */  
   OpDesc:string,
      /**  Kit Date. Not directly maintanable. Updated via the scheduling process.  */  
   KitDate:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Booked Unit Cost  */  
   BookedUnitCost:number,
      /**   Initially defaulted to false. This flag is set to true at the time JobOper.ProdComplete is set to true if JobHead.ProductionYield = true and OpMaster. PrdYldRecalcExpected = true and the actual completed qty for the operation vs. the expected completion qty is out of variance based on the under percentage set in OpMaster. This flag is used by the production yield recalculation logic to determine if recalculation is required for a job.
This field is maintained by the system only.  */  
   RecalcExpProdYld:boolean,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  When true this would signify that this operation was rough cut scheduled - meaning the operation would have start and end dates but no supporting resourcetimeused or shopload records.  */  
   RoughCutSched:boolean,
      /**  Scheduling Comments  */  
   SchedComment:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableLaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt2LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt3LaborRate:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
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
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   TearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   TearDwnEndHour:number,
      /**  Scheduled tear down start date. The start date would be the production end date.  */  
   WITearDwnEndDate:string,
      /**  Scheduled tear down due hour offset from the end of the prodution time.  This field is established by scheduling.  */  
   WITearDwnEndHour:number,
   UseAllRoles:boolean,
      /**  The PartNum for the asset. This should be disabled for a service call job, in which case the asset information would be transferred from the service call line when an operation is created for the job.  */  
   AssetPartNum:string,
      /**  Serial number of the asset.  */  
   SerialNumber:string,
      /**  ActualStartDate  */  
   ActualStartDate:string,
      /**  ActualStartHour  */  
   ActualStartHour:number,
      /**  ActualEndDate  */  
   ActualEndDate:string,
      /**  ActualEndHour  */  
   ActualEndHour:number,
      /**  FSJobStatus  */  
   FSJobStatus:number,
      /**  Instructions  */  
   Instructions:string,
      /**  ProdUOM  */  
   ProdUOM:string,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:boolean,
      /**  RemovedfromPlan  */  
   RemovedfromPlan:boolean,
      /**  EstStdType  */  
   EstStdType:number,
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
      /**  MobileOperation  */  
   MobileOperation:boolean,
      /**  ReWork  */  
   ReWork:boolean,
      /**  RequestMove  */  
   RequestMove:boolean,
      /**  ContractID  */  
   ContractID:string,
      /**  PrinterID  */  
   PrinterID:string,
      /**  LastPrintedDate  */  
   LastPrintedDate:string,
      /**  LastPCIDPrinted  */  
   LastPCIDPrinted:string,
      /**  CurrentPkgCode  */  
   CurrentPkgCode:string,
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
      /**  The identification of related StageNo.  */  
   StageNumber:string,
      /**  TemplateID  */  
   TemplateID:string,
      /**  The sum of LaborDtl ScrapQty for this operation.  */  
   ActScrapQty:number,
      /**  Auto receive flag  */  
   AutoReceive:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  The currency switch flag.  */  
   CurrencySwitch:boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
   DisplayExtPrice:number,
      /**  The display service amount.  */  
   DisplayServAmt:number,
      /**  The display service labor rate  */  
   DisplayServLaborRate:number,
      /**  Calculated display unit price  */  
   DisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  The converted display service amount.  */  
   DocDisplayServAmt:number,
      /**  The converted display service labor rate.  */  
   DocDisplayServLaborRate:number,
      /**  The document display unit price  */  
   DocDisplayUnitPrice:number,
      /**  Display IUM field (readonly)  */  
   DspIUM:string,
      /**  Field to determine to enable or disable autoreceive.  */  
   EnableAutoReceive:boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  This external field is used as a flag to determine when to enable/disable the SNRequiredSubConShip field on UI screen.  */  
   EnableSNReqSubConShip:boolean,
   EnableSNRequiredOpr:boolean,
      /**  For non subconctract operations JobOper.EstSetHours * JobOper.SetupBurRate + JobOper.EstProdHours * JobOper.ProdBurRate  */  
   EstBurdenCost:number,
      /**  The calculated estimated labor hours  */  
   EstLabHours:number,
      /**  For non subcontract operations : JobOper.EstSetHours * JobOper.SetupCrewSize * JobOper.SetupLabRate +JobOper.EstProdHours * JobOper.ProdCrewSize * JobOper.ProdLabRate  */  
   EstLaborCost:number,
      /**  For SubContract operations: JobOper.EstUnitCost * JobOper.RunQty  */  
   EstSubCost:number,
      /**  Final operation  */  
   FinalOpr:boolean,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
      /**  This is the description of the Method for Labor Entry.  Can be "Time and Quantity" for 'T', "Quantity Only" for 'Q', "Backflush" for 'B' or "Time and Backflush Qty" for 'X'  */  
   LaborEntryMethodDesc:string,
      /**  The total Load Hours calculated by summing the SetUpLoadHrs + ProdLoadHrs.  */  
   LoadHrs:number,
   OpStdDescription:string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimaryProdOpDtlDesc:string,
      /**  Primary Resource Group Description  */  
   PrimaryResourceGrpDesc:string,
      /**  The Resource Group ID of the primary production operation detail.  */  
   PrimaryResourceGrpID:string,
      /**  Description is initially created when the JobOpDtl is created.   If the JobOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  */  
   PrimarySetupOpDtlDesc:string,
      /**  The calculated production quantity  */  
   ProductionQty:number,
      /**  Indicates if the scheduling resources should be refreshed when the op code changes.  */  
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
      /**  The calculated scrap quantity  */  
   ScrapQty:number,
      /**  Contains the value of which icon to display in tree for joboper  */  
   ShowStatusIcon:string,
      /**  StdBasis Description  */  
   StdBasisDescription:string,
      /**  StdFormat Description  */  
   StdFormatDescription:string,
      /**  For SubContract Operations equals to the ActLaborCost  */  
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Job Number. Used in tying record back to its parent JobHead record.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  */  
   PartsPerOp:number,
      /**   The number of individual parts that are being produced
part. Sum of all related JobProd.ProdQty.
Not Directly maintable.  */  
   PartQty:number,
      /**  Part Qty that is being produced for Stock.  */  
   StockQty:number,
      /**   Total Quantity of the end part shipped from this job.
Updated via the ShipDtl write triggers.  */  
   ShippedQty:number,
      /**   Total quantity received to stock for the end part of the Job.
Updated via the Manufacturing receipts process.  */  
   ReceivedQty:number,
      /**   Represents the "outstanding" WIP of production quantity.
A summary of JobProd.WIPQty, updated via JobProd write trigger.  */  
   WIPQty:number,
      /**   Part Production quantity completed.
Updated via JobOper write trigger or LaborPart trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Quantity of the job completed quantity that is "Reserved" for the linked demands (sales orders/other jobs). Summary of PartAlloc.ReservedQty where PartAlloc.SupplyJobNum = JobHead.JobNum.  Reservations for Orders are made via the Order Allocations program. They are excluded from available quantity calculations for the job. Available Quantity = JobHead.QtyCompleted - (Shipped + Received to stk + ReservedAllocQty + PickingQty + PickedQty).  Maintained via PartAlloc write trigger.  */  
   ReservedQty:number,
      /**  Total Allocated Quantity for this job part  */  
   AllocatedQty900:number,
      /**  Quantity of the job completed quantity that is considered as in the "Picking" process for the linked sales orders. Summary of PartAlloc.PickingQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickingQty is set in the Order Allocation program. Maintained via PartAlloc write trigger.  */  
   PickingQty:number,
      /**  Quantity of the job completed quantity that is considered as in the shipping "Staging" process for the linked sales orders. Summary of PartAlloc.PickedQty where PartAlloc.SupplyJobNum = JobHead.JobNum. PickedQty is updated when the material move moves the item to the staging area.  Maintained via PartAlloc write trigger.  */  
   PickedQty:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   LbrCostBase:number,
      /**   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  */  
   MtlCostBase:number,
      /**  Indicates if Job is closed.  Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   JobClosed:boolean,
      /**  Indicates if production is complete for the job.   Mirror image of JobHead.JobClosed. Duplicated for performance reasons  */  
   JobComplete:boolean,
      /**  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  */  
   Plant:string,
      /**  Describes the Part.  */  
   PartDescription:string,
      /**  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  */  
   IUM:string,
      /**   Shipping Documents Required.
Indicates if shipping documents are required when shipping this part from the Job. Pertains to Job Shipments only and only if the PartNum does not exist in the PartTable. If it does exist then the Part.ShipDocReq. If checked, then at the time of shipping the system will require that the JobPart.ShipDocsAvail flag is true before allowing the shipment.Requires DocManagement license.  */  
   ShipDocReq:boolean,
      /**   Required Shipping Documents Available.
A flag manually set by the user to indicate that the required documents for the Job Part  are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Job Part.  If the Part.ShipDocReq = yes  then JobPart.ShipDocsA vail must = yes before the system will allow shipment of the Part from the job.Requires DocManagement license.  */  
   ShipDocAvail:boolean,
      /**  List of materials that us this part as cost base  */  
   MtlList:string,
      /**  Indicates that MRP should not create job suggestions for the specified co-part  */  
   PreventSugg:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   OrderQty:number,
      /**  The value of the JobHead.ProcessMode  */  
   ProcessMode:string,
      /**  Indicates if ShipDocReq is enabled. Only if JobPart.PartNum does not exist in Part Table and if Document Management is installed.  */  
   EnableShipDocReq:boolean,
      /**  Logical field signifying whether JobPart.PartNum is a valid part master part.  */  
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobClosingList_input{
   ds:Erp_Tablesets_JobClosingListTableset[],
}

export interface GetNewJobClosingList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingListTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobClosing_input{
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface GetNewJobClosing_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
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
      @param ds
   */  
export interface OnChangeJobClosed_input{
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface OnChangeJobClosed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeJobCompletion_input{
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface OnChangeJobCompletion_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
}
}

   /** Required : 
      @param pcJobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  Job # selected  */  
   pcJobNum:string,
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreCloseJob_input{
   ds:Erp_Tablesets_JobClosingTableset[],
}

export interface PreCloseJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingTableset[],
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param jobNum
   */  
export interface SelectJobByJobNum_input{
      /**  Closing JobNum.  */  
   jobNum:string,
}

export interface SelectJobByJobNum_output{
   returnObj:Erp_Tablesets_JobClosingTableset[],
}

   /** Required : 
      @param ds
   */  
export interface SelectMultipleJob_input{
   ds:Erp_Tablesets_JobClosingListTableset[],
}

export interface SelectMultipleJob_output{
   returnObj:Erp_Tablesets_JobClosingTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobClosingListTableset[],
}
}

