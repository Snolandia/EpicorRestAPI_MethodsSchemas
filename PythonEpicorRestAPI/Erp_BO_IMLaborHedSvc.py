import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMLaborHedSvc
# Description: Business Object to handle: Add, Update and Delete of LaborHed, LaborDtl
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AddIndirectLabor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddIndirectLabor
   Description: Add LaborHed and LaborHed related tables
   OperationID: AddIndirectLabor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddIndirectLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddIndirectLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteIndirectLabor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteIndirectLabor
   Description: Delete LaborHed and LaborHed related tables
   OperationID: DeleteIndirectLabor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteIndirectLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteIndirectLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateIndirectLabor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateIndirectLabor
   Description: Update LaborHed and LaborHed related tables
   OperationID: UpdateIndirectLabor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateIndirectLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateIndirectLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMLaborHedSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddIndirectLabor_input:
   """ Required : 
   IMLaborHedTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   saveAddOnError
   imIntegrationKey
   """  
   def __init__(self, obj):
      self.IMLaborHedTableset:list[Erp_Tablesets_IMLaborHedTableset] = obj["IMLaborHedTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.saveAddOnError:bool = obj["saveAddOnError"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

class AddIndirectLabor_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

      """  output parameters  """  

class DeleteIndirectLabor_input:
   """ Required : 
   IMLaborHedTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMLaborHedTableset:list[Erp_Tablesets_IMLaborHedTableset] = obj["IMLaborHedTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class DeleteIndirectLabor_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMIntegrationKeyRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      """  The master file which the integration is related to.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMIntegrationKeyTableset:
   def __init__(self, obj):
      self.IMIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyRow] = obj["IMIntegrationKey"]
      self.IMNaturalKeys:list[Erp_Tablesets_IMNaturalKeysRow] = obj["IMNaturalKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMLaborDtlCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The unique identifier of the Labor Header the comment relates to.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key for related IntQueInOut  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is a GUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMLaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key from related IntQueInOut  """  
      self.CallCode:str = obj["CallCode"]
      """  Used by Epicor FSA  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Used by Epicor FSA  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Used by Epicor FSA  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Field Service Contract Num  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMLaborHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  The number of the employee that performed the work. This field is directly maintainable. A selection list is provided in labor entry to find the employee by name.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  An integer assigned by the system to uniquely identify the LaborHed record. This integer is created by using the database sequence "LaborHedSeq".  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """   The Payroll date is the "Logical Day" that labor occurred. In most cases this is the same as the "Physical Day".  But when work is done before and after midnight then "Labor Collection" rolls the physical date forward or backward to create a Logical date. This date will be used to group transactions together by a logical date in order to calculate daily overtime during the transfer to payroll.
It will also be used in the selection criteria logic during the transfer to payroll.  This is duplicated into each LaborDtl.  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date of the clock in time field. It is created using the ActualDate and may be rolled forward/backward if the clock in time is adjusted across midnight. For example, when an employee clocks in prior to midnight, but shift starts at midnight or later, this situation causes the default to be ActualDateIn + 1.  """  
      self.ClockInTime:int = obj["ClockInTime"]
      """  The clock in time to be considered for payroll and costing purposes as the time when the employee starts work. Clock in time is stored as Hours.Hundreths. It is created using the ActualClockIn value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockin" is before the shift start time (JCShift.Start) and after ( JCShift. start - JCSyst.Grace) then the system adjusts the clockin time to be the start of the shift. Else it will be set to the actual system time.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockInTime:int = obj["ActualClockInTime"]
      """  Actual clock in time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocked in. In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.StartTime. Stored as Hours:Hundreths.  """  
      self.ActualClockinDate:str = obj["ActualClockinDate"]
      """  The actual date at the time of clockin. Labor Collection uses the system date to create this field.  Labor entry allows entry of this field and then uses it to generate the default for the adjusted  "ClockInDate".  This field is provided mainly for audit purposes.  """  
      self.LunchStatus:str = obj["LunchStatus"]
      """   An internal control byte used by Labor Collection when the system is configured not to take out lunch automatically (JCSyst.AutoLunch = N). It is used determine if what to do when the "Lunch" button is pressed.

The possible values are "N" - No lunch, "O" - Out to Lunch, "R" - Returned from lunch.  """  
      self.ActLunchOutTime:int = obj["ActLunchOutTime"]
      """   Actual Clock out time for Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchStart as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time for LunchOut.  """  
      self.LunchOutTime:int = obj["LunchOutTime"]
      """   Clock out time for Lunch that is used for costing/payroll determination. It is created by adjusting the ActLunchOutTime. . The adjusted time is where the system time is rolled back to the JCShift.LunchStart time when the employee clocks out for lunch after it has started but before it ends.

Stored as Hours.Hundreths.  """  
      self.ActLunchInTime:int = obj["ActLunchInTime"]
      """   Actual Clock In  time from Lunch.  Stored as Hours.Hundreths.  If the system is configured to automatically take out the standard lunch time (JCSyst.AutoLunch = Yes) then use the JCShift.LunchEnd as the default. Labor collection creates these during the clock In function. But may erase or adjust them if the employee clocks out before or during the lunch period.

If JCsyst.AutoLunch = "NO"  then there is no default.

Labor entry  validates that the LunchOut  -  LunchIn falls between the ClockIn and ClockOut times. 

If the JCSyst.AutoLunch = "NO" then Labor Collection allows the Lunch Clock in/out function and captures the system time.  """  
      self.LunchInTime:int = obj["LunchInTime"]
      """   Clock In time from Lunch break that is used for costing/payroll determination. Created by adjusting the ActLunchInTime.
The adjusted time is where the system time is rolled forward to the JCShift.LunchEnd time when the employee clocks in from lunch before the lunch period ends. 
Stored as Hours.Hundreths.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """  The clockOut in time to be considered for payroll and costing purposes as the time when the employee stops work. ClockOut time is stored as Hours.Hundreths. It is defaulted using the ActualClockOut value & the Grace period allowed (JCSyst.Grace).  If the "ActualClockOut" is after the shift end time (JCShift.End) and before ( JCShift.End + JC.Syst.Grace) then the system adjusts the ClockOut time to be the end of the shift. Else it will be set to the actual system time.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ActualClockOutTime:int = obj["ActualClockOutTime"]
      """  Actual clock Out time. This time is NOT ADJUSTED, Labor collection uses the actual physical system time when the employee clocks out.  In Labor Entry it would be entered from the TimeCard. Labor entry defaults it to the JCShift.EndTime. Stored as Hours.Hundreths.  """  
      self.PayHours:int = obj["PayHours"]
      """   Hours for payroll.  This is stored as Hours.Hundreths. For example 3 1/2 hours is stored as 3.5. This is calculated when the Start/Stop times are changed in labor entry. It can then be overridden.
The Logic for calculating hours from clockin, clockout is:
If ClockIn > ClockOut Gross Hours = ( (ClockOut + 24.00) - ClockIn) else Gross Hours = ClockOut - ClockIn. 
If LunchOut > LunchIn Lunch Hours = ( (LunchIn +24) - LunchOut )
else Lunch Hours = ( LunchIn - LunchOut ).
PayHours = GRoss Hours - Lunch Hours. 
Remember that the database clockin/clockout fields are stored as hours hundredths, while the entry widgets are either hours.hundreths or Hours:Minutes. So use the database fields in this calculation and there is no need to worry about conversions.  """  
      self.FeedPayroll:bool = obj["FeedPayroll"]
      """  Flag that indicates this labor transaction is eligible for transfer to DCD payroll application. The default is set from JCSyst.FeedPayroll.  """  
      self.TransferredToPayroll:bool = obj["TransferredToPayroll"]
      """  Indicates if this transaction has been transferred to payroll. This is updated via the Payroll function to transfer labor.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.TranSet:str = obj["TranSet"]
      """  An optional field where the user enters a string of characters that would be used to associate multiple transactions as being part of a transaction set. TranSet will be used for data selection type functions.  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborHed record is currently active. When the employee clocks out it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice, displaying which employees are clocked in and which ones have not clocked out. Labor entry can't access a record that is Open.  """  
      self.ChkLink:str = obj["ChkLink"]
      """   Encoded value PRChkDtl.HeadNum + PRChkDtl.LineNum.
Used to relate the labor to the payroll check detail.  """  
      self.BatchTotalHrsDisp:str = obj["BatchTotalHrsDisp"]
      """  BatchTotalHrsDisp  """  
      self.BatchHrsRemainDisp:str = obj["BatchHrsRemainDisp"]
      """  BatchHrsRemainDisp  """  
      self.BatchHrsRemainPctDisp:str = obj["BatchHrsRemainPctDisp"]
      """  BatchHrsRemainPctDisp  """  
      self.BatchSplitHrsMethod:str = obj["BatchSplitHrsMethod"]
      """  BatchSplitHrsMethod  """  
      self.BatchAssignTo:bool = obj["BatchAssignTo"]
      """  BatchAssignTo  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchStartHrs:str = obj["BatchStartHrs"]
      """  BatchStartHrs  """  
      self.BatchEndHrs:str = obj["BatchEndHrs"]
      """  BatchEndHrs  """  
      self.BatchTotalHrs:int = obj["BatchTotalHrs"]
      """  BatchTotalHrs  """  
      self.BatchHrsRemain:int = obj["BatchHrsRemain"]
      """  BatchHrsRemain  """  
      self.BatchHrsRemainPct:int = obj["BatchHrsRemainPct"]
      """  BatchHrsRemainPct  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key from related IntQueInOut  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMLaborHedTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMLaborDtl:list[Erp_Tablesets_IMLaborDtlRow] = obj["IMLaborDtl"]
      self.IMLaborHed:list[Erp_Tablesets_IMLaborHedRow] = obj["IMLaborHed"]
      self.IMLaborDtlComment:list[Erp_Tablesets_IMLaborDtlCommentRow] = obj["IMLaborDtlComment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMNaturalKeysRow:
   def __init__(self, obj):
      self.KeyValue:str = obj["KeyValue"]
      self.KeyColumn:str = obj["KeyColumn"]
      self.Sequence:int = obj["Sequence"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class UpdateIndirectLabor_input:
   """ Required : 
   IMLaborHedTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMLaborHedTableset:list[Erp_Tablesets_IMLaborHedTableset] = obj["IMLaborHedTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class UpdateIndirectLabor_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

