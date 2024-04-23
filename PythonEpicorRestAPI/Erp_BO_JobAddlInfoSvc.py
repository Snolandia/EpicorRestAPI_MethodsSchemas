import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobAddlInfoSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Overrides(epicorHeaders = None):
   """  
   Summary: Invoke method Overrides
   OperationID: Overrides
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Overrides_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetJobInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobInfo
   Description: Returns Job Add Info details
   OperationID: GetJobInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOperations(epicorHeaders = None):
   """  
   Summary: Invoke method GetOperations
   Description: Returns Operations data set
   OperationID: GetOperations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetResourceGroups(epicorHeaders = None):
   """  
   Summary: Invoke method GetResourceGroups
   Description: Returns Resource Groups data set
   OperationID: GetResourceGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResourceGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAddlInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_JobAddInfoDtlRow:
   def __init__(self, obj):
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobAddlInfoRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.ProdQty:int = obj["ProdQty"]
      self.DrawNum:str = obj["DrawNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.StartDate:str = obj["StartDate"]
      self.DueDate:str = obj["DueDate"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.AsmDescription:str = obj["AsmDescription"]
      self.AsmRequiredQty:int = obj["AsmRequiredQty"]
      self.AsmDrawNum:str = obj["AsmDrawNum"]
      self.AsmRevisionNum:str = obj["AsmRevisionNum"]
      self.AsmStartDate:str = obj["AsmStartDate"]
      self.AsmDueDate:str = obj["AsmDueDate"]
      self.OprOPDesc:str = obj["OprOPDesc"]
      self.OprRunQty:int = obj["OprRunQty"]
      self.OprQtyLeft:int = obj["OprQtyLeft"]
      self.OprSetupLeft:int = obj["OprSetupLeft"]
      self.OprEstSetHours:int = obj["OprEstSetHours"]
      self.OprSetupCrewSize:int = obj["OprSetupCrewSize"]
      self.OprProdStandard:int = obj["OprProdStandard"]
      self.OprStdFormat:str = obj["OprStdFormat"]
      self.OprStdBasis:str = obj["OprStdBasis"]
      self.OprOpsPerPart:int = obj["OprOpsPerPart"]
      self.OprProdCrewSize:int = obj["OprProdCrewSize"]
      self.OprStartDate:str = obj["OprStartDate"]
      self.OprDueDate:str = obj["OprDueDate"]
      self.OprMachines:int = obj["OprMachines"]
      self.ActEmp:str = obj["ActEmp"]
      self.JobComments:str = obj["JobComments"]
      self.AsmComments:str = obj["AsmComments"]
      self.OprComments:str = obj["OprComments"]
      self.JobNum:str = obj["JobNum"]
      self.Asm:int = obj["Asm"]
      self.Opr:int = obj["Opr"]
      self.JobAsmOpr:str = obj["JobAsmOpr"]
      self.OprInstructions:str = obj["OprInstructions"]
      self.OprQtyPerCycle:int = obj["OprQtyPerCycle"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobAddlInfoTableset:
   def __init__(self, obj):
      self.JobAddlInfo:list[Erp_Tablesets_JobAddlInfoRow] = obj["JobAddlInfo"]
      self.JobOperAction:list[Erp_Tablesets_JobOperActionRow] = obj["JobOperAction"]
      self.JobOperActionParam:list[Erp_Tablesets_JobOperActionParamRow] = obj["JobOperActionParam"]
      self.JobAddInfoDtl:list[Erp_Tablesets_JobAddInfoDtlRow] = obj["JobAddInfoDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobOperActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  Data type of Action Parameter.  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JobOperActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number which uniquely identifies the assembly record within the method.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this action must be completed before Operation can be completed.  """  
      self.Completed:bool = obj["Completed"]
      """  Indicates if this Action was completed.  """  
      self.CompletedBy:str = obj["CompletedBy"]
      """  The number of the employee that performed the work.  """  
      self.CompletedOn:str = obj["CompletedOn"]
      """  Date the Action was completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  """  
      self.BuyerName:str = obj["BuyerName"]
      self.OPType:str = obj["OPType"]
      """  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  """  
      self.AllowInCurPlant:bool = obj["AllowInCurPlant"]
      self.Subcontract:bool = obj["Subcontract"]
      """  SubContract Operation  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasCharacteristics:bool = obj["HasCharacteristics"]
      """  Operation has Characteristics  """  
      self.HasActions:bool = obj["HasActions"]
      """  Operations has some Actions.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OperationsTableset:
   def __init__(self, obj):
      self.OpMasterList:list[Erp_Tablesets_OpMasterListRow] = obj["OpMasterList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ResourceGroupListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Long description of the Resource Group.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Flag which indicates if the Resource Group is considered "Inactive".  For historical purposed, and data integrity, it is difficult to delete a ResourceGroup that has been used for production.  Instead, it is set to Inactive = YES.
This flag will be used to exclude Resource Groups from certain searches and reports.
Resource Groups where Inactive=yes are treated as deleted, but remain in the table to maintain database integrity.  """  
      self.JCDept:str = obj["JCDept"]
      """  The Key ID of the Home Department for this Resource Group.  This is a foreign key to the JCDept table.  """  
      self.ProdBurRate:int = obj["ProdBurRate"]
      """  The burden rate for production.  """  
      self.SetupBurRate:int = obj["SetupBurRate"]
      """  Default burden rate for Setup time.  """  
      self.QProdBurRate:int = obj["QProdBurRate"]
      """   Quoting burden rate for production in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.QSetupBurRate:int = obj["QSetupBurRate"]
      """   Quoting burden rate for setup in the Resource Group.
Based on QBurdenType this may be an hourly rate or a percentage.  """  
      self.ResourceType:str = obj["ResourceType"]
      """  For scheduling purposes a Resource Group can be a Standard resource (S), Additional resource (D), or Auxiliary resource (X).  Standard resources use capacity when scheduled in a finite capacity workcenter.  An Auxiliary Resource can be used in production by  any operation concurrently with a Standard resource, but it does not use capacity.  This is significant for scheduling work to the machine.  Also, an Auxiliary resources does not have to be available for an entire operation.  Additional resources can be added to an Operation, they do use capacity and need to be available for the entire operation.  """  
      self.InputWhse:str = obj["InputWhse"]
      """  Indicates a warehouse  in which parts are staged for consumption by the Resource Group.  This must be valid in the Warehouse table.  """  
      self.OutputWhse:str = obj["OutputWhse"]
      """  Defines a warehouse for the output of a Resource Group.  This must be valid in the Warehouse table.  """  
      self.Location:bool = obj["Location"]
      """  Location  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ResourceGroupsTableset:
   def __init__(self, obj):
      self.ResourceGroupList:list[Erp_Tablesets_ResourceGroupListRow] = obj["ResourceGroupList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetJobInfo_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   ipOprSeq
   ipCrewCount
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job number  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  Assembly Seq  """  
      self.ipOprSeq:int = obj["ipOprSeq"]
      """  Opr Seq  """  
      self.ipCrewCount:int = obj["ipCrewCount"]
      """  Crew Count  """  
      pass

class GetJobInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobAddlInfoTableset] = obj["returnObj"]
      pass

class GetOperations_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OperationsTableset] = obj["returnObj"]
      pass

class GetResourceGroups_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ResourceGroupsTableset] = obj["returnObj"]
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

class Overrides_output:
   def __init__(self, obj):
      pass

