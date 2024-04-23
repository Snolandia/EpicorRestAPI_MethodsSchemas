import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JobAsmblCostsSvc
# Description: Logic to retrieve Hours and Costs for Job Assemblies
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmblCostsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmblCostsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetJobAsmblCosts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobAsmblCosts
   Description: Retrieves the Hours and Costs for a Job Assembly
   OperationID: GetJobAsmblCosts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobAsmblCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobAsmblCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JobAsmblCostsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_JobAsmblCostsTableset:
   def __init__(self, obj):
      self.JobCosts:list[Erp_Tablesets_JobCostsRow] = obj["JobCosts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobCostsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.LLABurdenCost:int = obj["LLABurdenCost"]
      """  Lower Level Burden Labor Cost.  """  
      self.LLALaborCost:int = obj["LLALaborCost"]
      """  Lower Level Actual Labor Cost.  """  
      self.LLAMaterialBurCost:int = obj["LLAMaterialBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLAMaterialCost:int = obj["LLAMaterialCost"]
      """  Lower Level Actual Material Cost.  """  
      self.LLAMaterialLabCost:int = obj["LLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  """  
      self.LLAMaterialMtlCost:int = obj["LLAMaterialMtlCost"]
      """  Lower Level Actual Material Material Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  """  
      self.LLAMaterialSubCost:int = obj["LLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  """  
      self.LLAMtlBurCost:int = obj["LLAMtlBurCost"]
      """  Lower Level Actual Material Burden Cost.  """  
      self.LLAProdHours:int = obj["LLAProdHours"]
      """  Lower Level Actual Production Hours.  """  
      self.LLASetupHours:int = obj["LLASetupHours"]
      """  Lower Level Actual Setup Hours.  """  
      self.LLASubcontractCost:int = obj["LLASubcontractCost"]
      """  Lower Level Actual Subcontractor Cost.  """  
      self.LLEBurdenCost:int = obj["LLEBurdenCost"]
      """  Lower Level Estimated Burden Cost.  """  
      self.LLELaborCost:int = obj["LLELaborCost"]
      """  Lower Level Estimated Labor Cost.  """  
      self.LLEMaterialCost:int = obj["LLEMaterialCost"]
      """  Lower Level Estimated Material Cost.  """  
      self.LLEMtlBurCost:int = obj["LLEMtlBurCost"]
      """  Lower Level Estimated Material Burden Cost.  """  
      self.LLEProdHours:int = obj["LLEProdHours"]
      """  Lower Level Est Prod. Hrs  """  
      self.LLESetupHours:int = obj["LLESetupHours"]
      """  Lower Level Estimated Setup Hours.  """  
      self.LLESubcontractCost:int = obj["LLESubcontractCost"]
      """  Lower Level Estimated Subcontract Cost.  """  
      self.PActTotalHours:int = obj["PActTotalHours"]
      """  Asembly Total Actual Production Hours (TLAProdHours + LLAProdHours)  """  
      self.PEstTotalHours:int = obj["PEstTotalHours"]
      """  Assembly Total Estimated Production Hours (TLEProdHours + LLEProdHours)  """  
      self.SActTotalHours:int = obj["SActTotalHours"]
      """  Assembly Total Actual Setup Hours (TLASetupHours + LLASetupHours)  """  
      self.SEstTotalHours:int = obj["SEstTotalHours"]
      """  Assembly Total Estimated Setup Hours (TLESetupHours + LLESetupHours)  """  
      self.TActBurCost:int = obj["TActBurCost"]
      """  Burden Actual Assembly Totals (TLABurdenCost + LLABurdenCost)  """  
      self.TActLabCost:int = obj["TActLabCost"]
      """  Labor Actual Assembly Totals (TLALaborCost + LLALaborCost)  """  
      self.TActLowerHours:int = obj["TActLowerHours"]
      """  Lower Level Actual Total Hours (LLASetupHours + LLAProdHours)  """  
      self.TActMtlBurCost:int = obj["TActMtlBurCost"]
      """  Material Burden Actual Assembly Totals (TLAMtlBurCost + LLAMtlBurCost)  """  
      self.TActMtlCost:int = obj["TActMtlCost"]
      """  Material Actual Assembly Totals (TLAMaterialCost + LLAMaterialCost)  """  
      self.TActSubCost:int = obj["TActSubCost"]
      """  Subcontract Actual Assembly Totals (TLASubcontractCost + LLASubcontractCost)  """  
      self.TActThisHours:int = obj["TActThisHours"]
      """  This Level Actual Total Hours (TLASetupHours + TLAProdHours)  """  
      self.TActTotalCost:int = obj["TActTotalCost"]
      """  Total Actual Assembly Totals (TActMtlCost + TActLabCost + TActBurCost + TActSubCost + TActMtlBurCost)  """  
      self.TActTotalHours:int = obj["TActTotalHours"]
      """  Assembly Total Actual Total Hours (SActTotalHours + PActTotalHours)  """  
      self.TDtlBurCost:int = obj["TDtlBurCost"]
      """  Burden Detail Assembly Totals  """  
      self.TDtlLabCost:int = obj["TDtlLabCost"]
      """  Labor Detail Assembly Totals  """  
      self.TDtlMtlBurCost:int = obj["TDtlMtlBurCost"]
      """  Material Burden Detail Assembly Totals  """  
      self.TDtlMtlCost:int = obj["TDtlMtlCost"]
      """  Material Detail Assembly Totals  """  
      self.TDtlSubCost:int = obj["TDtlSubCost"]
      """  Subcontract Detail Assembly Totals  """  
      self.TEstBurCost:int = obj["TEstBurCost"]
      """  Burden Estimated Assembly Totals (TLEBurdenCost + LLEBurdenCost)  """  
      self.TEstLabCost:int = obj["TEstLabCost"]
      """  Labor Estimated Assembly Totals (TLELaborCost + LLELaborCost)  """  
      self.TEstLowerHours:int = obj["TEstLowerHours"]
      """  Lower Level Estimated Total Hours (LLESetupHours + LLEProdHours)  """  
      self.TEstMtlBurCost:int = obj["TEstMtlBurCost"]
      """  Material Burden Estimated Assembly Totals (TLEMtlBurCost + LLEMtlBurCost)  """  
      self.TEstMtlCost:int = obj["TEstMtlCost"]
      """  Material Estimated Assembly Totals (TLEMaterialCost + LLEMaterialCost)  """  
      self.TEstSubCost:int = obj["TEstSubCost"]
      """  Subcontract Estimated Assembly Totals (TLESubcontractCost + LLESubcontractCost)  """  
      self.TEstThisHours:int = obj["TEstThisHours"]
      """  This Level Estimated Total Hours (TLESetupHours + TLEProdHours)  """  
      self.TEstTotalCost:int = obj["TEstTotalCost"]
      """  Total Estimated Assembly Totals (TEstMtlCost + TEstLabCost + TEstBurCost + TEstSubCost + TEstMtlBurCost)  """  
      self.TEstTotalHours:int = obj["TEstTotalHours"]
      """  Assembly Total Estimated Total Hours (SEstTotalHours + PEstTotalHours)  """  
      self.TLABurdenCost:int = obj["TLABurdenCost"]
      """  This Level Actual Burden Cost.  """  
      self.TLALaborCost:int = obj["TLALaborCost"]
      """  This Level Actual Labor Cost  """  
      self.TLAMaterialBurCost:int = obj["TLAMaterialBurCost"]
      """  This Level Actual Material Burden Cost. TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost = TLAMaterialCost.  """  
      self.TLAMaterialCost:int = obj["TLAMaterialCost"]
      """  This Level Actual Material Cost  """  
      self.TLAMaterialLabCost:int = obj["TLAMaterialLabCost"]
      """  Lower Level Actual Material Labor Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  """  
      self.TLAMaterialMtlCost:int = obj["TLAMaterialMtlCost"]
      """  This Level Actual Material Mtl. Cost  """  
      self.TLAMaterialSubCost:int = obj["TLAMaterialSubCost"]
      """  Lower Level Actual Material Subcontract Cost. LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost = LLAMaterialCost.  """  
      self.TLAMtlBurCost:int = obj["TLAMtlBurCost"]
      """  This Level Actual Material Burden Cost  """  
      self.TLAProdHours:int = obj["TLAProdHours"]
      """  This Level Actual Prod. Hrs  """  
      self.TLASetupHours:int = obj["TLASetupHours"]
      """  This Level Actual Setup Hours.  """  
      self.TLASubcontractCost:int = obj["TLASubcontractCost"]
      """  This Level Actual Subcontract Cost.  """  
      self.TLEBurdenCost:int = obj["TLEBurdenCost"]
      """  This Level Est Burden Cost  """  
      self.TLELaborCost:int = obj["TLELaborCost"]
      """  This Level Est Labor Cost  """  
      self.TLEMaterialCost:int = obj["TLEMaterialCost"]
      """  This Level Estimated Material Cost.  """  
      self.TLEMtlBurCost:int = obj["TLEMtlBurCost"]
      """  This Level Est Material Burden Cost  """  
      self.TLEProdHours:int = obj["TLEProdHours"]
      """  This Level Estimated Production Hours.  """  
      self.TLESetupHours:int = obj["TLESetupHours"]
      """  This Level Estimated Setup Hours.  """  
      self.TLESubcontractCost:int = obj["TLESubcontractCost"]
      """  This Level Est Subcontract Cost  """  
      self.TLAMaterialMtlBurCost:int = obj["TLAMaterialMtlBurCost"]
      """  This Level Actual Component Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  """  
      self.LLAMaterialMtlBurCost:int = obj["LLAMaterialMtlBurCost"]
      """  Lower Level Actual Component Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  """  
      self.LLCMaterialCost:int = obj["LLCMaterialCost"]
      """  Lower Level Material Cost Element.  This is the difference between the Actual Material Cost (LLAMaterialCost) and the Component Material Cost (LLAMaterialMtlCost).  """  
      self.LLCLaborCost:int = obj["LLCLaborCost"]
      """  Lower Level Labor Cost Element.  This is the difference between the Actual Labor Cost (LLALaborCost) and the Component Labor Cost (LLAMaterialLabCost).  """  
      self.LLCBurdenCost:int = obj["LLCBurdenCost"]
      """  Lower Level Burden Cost Element.  This is the difference between the Actual Burden Cost (LLABurdenCost) and the Component Burden Cost (LLAMaterialBurCost).  """  
      self.LLCSubcontractCost:int = obj["LLCSubcontractCost"]
      """  Lower Level Subcontract Cost Element.  This is the difference between the Actual Subcontract Cost (LLASubcontractCost) and the Component Subcontract Cost (LLAMaterialSubCost).  """  
      self.LLCMtlBurCost:int = obj["LLCMtlBurCost"]
      """  Lower Level Material Cost Element.  This is the difference between the Actual Material Burden Cost (LLAMtlBurCost) and the Component Material Burden Cost (LLAMaterialMtlBurCost).  """  
      self.TCmpMaterialCost:int = obj["TCmpMaterialCost"]
      """  Material Cost Element Assembly Totals (TActMtlCost - TDtlMtlCost)  """  
      self.TCmpLaborCost:int = obj["TCmpLaborCost"]
      """  Labor Cost Element Assembly Totals (TActLabCost - TDtlLabCost)  """  
      self.TCmpBurdenCost:int = obj["TCmpBurdenCost"]
      """  Burden Cost Element Assembly Totals (TActBurCost - TDtlBurCost)  """  
      self.TCmpSubcontractCost:int = obj["TCmpSubcontractCost"]
      """  Subcontract Cost Element Assembly Totals (TActSubCost - TDtlSubCost)  """  
      self.TCmpMtlBurCost:int = obj["TCmpMtlBurCost"]
      """  Material Burden Cost Element Assembly Totals (TActMtlBurCost - TDtlMtlBurCost)  """  
      self.TLCMaterialCost:int = obj["TLCMaterialCost"]
      """  This Level Material Cost Element.  This is the difference between the Actual Material Cost (TLAMaterialCost) and the Component Material Cost (TLAMaterialMtlCost).  """  
      self.TLCLaborCost:int = obj["TLCLaborCost"]
      """  This Level Labor Cost Element.  This is the difference between the Actual Labor Cost (TLALaborCost) and the Component Labor Cost (TLAMaterialLabCost).  """  
      self.TLCBurdenCost:int = obj["TLCBurdenCost"]
      """  This Level Burden Cost Element.  This is the difference between the Actual Burden Cost (TLABurdenCost) and the Component Burden Cost (TLAMaterialBurCost).  """  
      self.TLCSubcontractCost:int = obj["TLCSubcontractCost"]
      """  This Level Subcontract Cost Element.  This is the difference between the Actual Subcontract Cost (TLASubcontractCost) and the Component Subcontract Cost (TLAMaterialSubCost).  """  
      self.TLCMtlBurCost:int = obj["TLCMtlBurCost"]
      """  This Level Material Burden Cost Element.  This is the difference between the Actual Material Burden Cost (TLAMtlBurCost) and the Component Material Burden Cost (TLAMaterialMtlBurCost).  """  
      self.LLAMfgCompMtlCost:int = obj["LLAMfgCompMtlCost"]
      """  Lower Level Actual Mfg Component Material Cost.  """  
      self.LLAMfgCompLabCost:int = obj["LLAMfgCompLabCost"]
      """  Lower Level Actual Mfg Component Labor Cost.  """  
      self.LLAMfgCompBurCost:int = obj["LLAMfgCompBurCost"]
      """  Lower Level Actual Mfg Component Burden Cost.  """  
      self.LLAMfgCompSubCost:int = obj["LLAMfgCompSubCost"]
      """  Lower Level Actual Mfg Component Subcontract Cost.  """  
      self.LLAMfgCompMtlBurCost:int = obj["LLAMfgCompMtlBurCost"]
      """  Lower Level Actual Mfg Component Material Burden Cost.  """  
      self.TLAMfgCompMtlCost:int = obj["TLAMfgCompMtlCost"]
      """  This Level Actual Mfg Component Material Cost.  """  
      self.TLAMfgCompLabCost:int = obj["TLAMfgCompLabCost"]
      """  This Level Actual Mfg Component Labor Cost.  """  
      self.TLAMfgCompBurCost:int = obj["TLAMfgCompBurCost"]
      """  This Level Actual Mfg Component Burden Cost.  """  
      self.TLAMfgCompSubCost:int = obj["TLAMfgCompSubCost"]
      """  This Level Actual Mfg Component Subcontract Cost.  """  
      self.TLAMfgCompMtlBurCost:int = obj["TLAMfgCompMtlBurCost"]
      """  This Level Actual Mfg Component Material Burden Cost.  """  
      self.TMfgBurCost:int = obj["TMfgBurCost"]
      """  Burden Mfg Element Assembly Totals (TLAMfgCompBurCost + LLAMfgCompBurCost)  """  
      self.TMfgLabCost:int = obj["TMfgLabCost"]
      """  Labor Mfg Element Assembly Totals (TLAMfgCompLabCost + LLAMfgCompLabCost)  """  
      self.TMfgMtlCost:int = obj["TMfgMtlCost"]
      """  Material Mfg Element Assembly Totals (TLAMfgCompMtlCost + LLAMfgCompMtlCost)  """  
      self.TMfgMtlBurCost:int = obj["TMfgMtlBurCost"]
      """  Material Burden Mfg Element Assembly Totals (TLAMfgCompMtlBurCost + LLAMfgCompMtlBurCost)  """  
      self.TMfgSubCost:int = obj["TMfgSubCost"]
      """  Subcontract Mfg Element Assembly Totals (TLAMfgCompSubCost + LLAMfgCompSubCost)  """  
      self.TLETotalCost:int = obj["TLETotalCost"]
      """  TLE Total Cost  """  
      self.TLСTotalCost:int = obj["TLСTotalCost"]
      """  TLС Total Cost  """  
      self.TLATotalCost:int = obj["TLATotalCost"]
      """  TLA Total Cost  """  
      self.TLAMfgCompTotalCost:int = obj["TLAMfgCompTotalCost"]
      """  TLAMfgComp Total Cost  """  
      self.TLAMaterialTotalCost:int = obj["TLAMaterialTotalCost"]
      """  TLA Material Total Cost  """  
      self.LLETotalCost:int = obj["LLETotalCost"]
      """  LLE Total Cost  """  
      self.LLCTotalCost:int = obj["LLCTotalCost"]
      """  LLC Total Cost  """  
      self.LLATotalCost:int = obj["LLATotalCost"]
      """  LLA Total Cost  """  
      self.LLAMfgCompTotalCost:int = obj["LLAMfgCompTotalCost"]
      """  LLA  MfgComp Total Cost  """  
      self.LLAMaterialTotalCost:int = obj["LLAMaterialTotalCost"]
      """  LLA Material Total Cost  """  
      self.TCmpTotalCost:int = obj["TCmpTotalCost"]
      """  TCmp Total Cost  """  
      self.TMfgTotalCost:int = obj["TMfgTotalCost"]
      """  TMfg Total Cost  """  
      self.TDtlTotalCost:int = obj["TDtlTotalCost"]
      """  TDtl Total Cost  """  
      self.TLCTotalCost:int = obj["TLCTotalCost"]
      """  TLC Total Cost  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetJobAsmblCosts_input:
   """ Required : 
   ipJobNum
   ipAssemblySeq
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Number  """  
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      """  Assembly Sequence  """  
      pass

class GetJobAsmblCosts_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JobAsmblCostsTableset] = obj["returnObj"]
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

