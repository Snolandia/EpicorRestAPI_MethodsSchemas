import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMEmpExpenseSvc
# Description: Business Object to handle: Add, Update, Delete of EmpExpense, EmpExpenseTax
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpExpenseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpExpenseSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AddIndirectEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddIndirectEmpExpense
   Description: Add EmpExpense related tables
   OperationID: AddIndirectEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddIndirectEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddIndirectEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMEmpExpenseSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddIndirectEmpExpense_input:
   """ Required : 
   IMEmpExpenseTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   saveAddOnError
   imIntegrationKey
   """  
   def __init__(self, obj):
      self.IMEmpExpenseTableset:list[Erp_Tablesets_IMEmpExpenseTableset] = obj["IMEmpExpenseTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.saveAddOnError:bool = obj["saveAddOnError"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

class AddIndirectEmpExpense_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMEmpExpenseCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense comment record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of  row in actual table  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMEmpExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The ap invoice number the expense was invoiced on.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExpenseAutoSubmit:bool = obj["ExpenseAutoSubmit"]
      """  ExpenseAutoSubmit  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.IntQueID:int = obj["IntQueID"]
      """  The IntQueID of the related IntQueIn  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMEmpExpenseTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMEmpExpense:list[Erp_Tablesets_IMEmpExpenseRow] = obj["IMEmpExpense"]
      self.IMEmpExpenseTax:list[Erp_Tablesets_IMEmpExpenseTaxRow] = obj["IMEmpExpenseTax"]
      self.IMEmpExpenseComment:list[Erp_Tablesets_IMEmpExpenseCommentRow] = obj["IMEmpExpenseComment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMEmpExpenseTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate code  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an expense.  When the sales tax field EcAquisition is checked then 2 expense tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.ExpReportableAmt:int = obj["ExpReportableAmt"]
      """  The reportable amount to the tax jurisdiction in the expense currency.  """  
      self.ExpTaxableAmt:int = obj["ExpTaxableAmt"]
      """  Taxable Amount for this expense in the expense currency  """  
      self.ExpTaxAmt:int = obj["ExpTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in the expense currency.  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is a GUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

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

