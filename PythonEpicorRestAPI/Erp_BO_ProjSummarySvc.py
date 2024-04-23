import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ProjSummarySvc
# Description: Project Management Code Master File. Establishes the valid Project Mgmt
code for the system. This file provides a description for the project
and allows user to set up project codes to be used during the order entry
and job entry process.
DELETING: Not allowed if referenced in the Job file, or Order files.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CalcSummaryOrdered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcSummaryOrdered
   Description: Culculates summary orders.
   OperationID: CalcSummaryOrdered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcSummaryOrdered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcSummaryOrdered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProjectCostsHours(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProjectCostsHours
   Description: Calculates Project cost hours
   OperationID: ProjectCostsHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProjectCostsHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProjectCostsHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjSummarySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CalcSummaryOrdered_input:
   """ Required : 
   curProjectID
   """  
   def __init__(self, obj):
      self.curProjectID:str = obj["curProjectID"]
      """  Project ID  """  
      pass

class CalcSummaryOrdered_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totord:int = obj["parameters"]
      self.totinv:int = obj["parameters"]
      self.totdep:int = obj["parameters"]
      self.totstkmtl:int = obj["parameters"]
      self.totstklbr:int = obj["parameters"]
      self.totstkbur:int = obj["parameters"]
      self.totstksub:int = obj["parameters"]
      self.totstkmbur:int = obj["parameters"]
      self.totactstk:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ProjSummaryTableset:
   def __init__(self, obj):
      self.ProjectCost:list[Erp_Tablesets_ProjectCostRow] = obj["ProjectCost"]
      self.ProjectHour:list[Erp_Tablesets_ProjectHourRow] = obj["ProjectHour"]
      self.ProjectSumry:list[Erp_Tablesets_ProjectSumryRow] = obj["ProjectSumry"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjectCostRow:
   def __init__(self, obj):
      self.ActMtlCost:int = obj["ActMtlCost"]
      self.ActSubCost:int = obj["ActSubCost"]
      self.Class:str = obj["Class"]
      self.ClassDescription:str = obj["ClassDescription"]
      self.EstMtlCost:int = obj["EstMtlCost"]
      self.EstSubCost:int = obj["EstSubCost"]
      self.ProjectID:str = obj["ProjectID"]
      self.QuotedMtlCost:int = obj["QuotedMtlCost"]
      self.QuotedSubCost:int = obj["QuotedSubCost"]
      self.EarnedMtlCost:int = obj["EarnedMtlCost"]
      self.EarnedSubCost:int = obj["EarnedSubCost"]
      self.EstMtlBurCost:int = obj["EstMtlBurCost"]
      self.ActMtlBurCost:int = obj["ActMtlBurCost"]
      self.EarnedMtlBurCost:int = obj["EarnedMtlBurCost"]
      self.ActODCCost:int = obj["ActODCCost"]
      """  Actual Other Direct Costs  """  
      self.EstODCCost:int = obj["EstODCCost"]
      """  Estimated Other Direct Cost  """  
      self.QuotedODCCost:int = obj["QuotedODCCost"]
      """  Quoted Other Direct cost  """  
      self.EarnedODCCost:int = obj["EarnedODCCost"]
      """  Earned Other Direct cost  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjectHourRow:
   def __init__(self, obj):
      self.ProjectID:str = obj["ProjectID"]
      self.JCDept:str = obj["JCDept"]
      self.DeptDescription:str = obj["DeptDescription"]
      self.EstBurHours:int = obj["EstBurHours"]
      self.EstLbrHours:int = obj["EstLbrHours"]
      self.QuotedBurHours:int = obj["QuotedBurHours"]
      self.QuotedLbrHours:int = obj["QuotedLbrHours"]
      self.ActBurHours:int = obj["ActBurHours"]
      self.ActLbrHours:int = obj["ActLbrHours"]
      self.EarnedBurHours:int = obj["EarnedBurHours"]
      self.EarnedLbrHours:int = obj["EarnedLbrHours"]
      self.QuotedLbrCost:int = obj["QuotedLbrCost"]
      self.QuotedBurCost:int = obj["QuotedBurCost"]
      self.EstLbrCost:int = obj["EstLbrCost"]
      self.EstBurCost:int = obj["EstBurCost"]
      self.ActLbrCost:int = obj["ActLbrCost"]
      self.ActBurCost:int = obj["ActBurCost"]
      self.EarnedLbrCost:int = obj["EarnedLbrCost"]
      self.EarnedBurCost:int = obj["EarnedBurCost"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjectSumryRow:
   def __init__(self, obj):
      self.EstMtl:int = obj["EstMtl"]
      self.EstLbr:int = obj["EstLbr"]
      self.EstBur:int = obj["EstBur"]
      self.EstSub:int = obj["EstSub"]
      self.EstMtlBur:int = obj["EstMtlBur"]
      self.ActMtl:int = obj["ActMtl"]
      self.ActLbr:int = obj["ActLbr"]
      self.ActBur:int = obj["ActBur"]
      self.ActSub:int = obj["ActSub"]
      self.ActMtlBur:int = obj["ActMtlBur"]
      self.EarnedMtl:int = obj["EarnedMtl"]
      self.EarnedLbr:int = obj["EarnedLbr"]
      self.EarnedBur:int = obj["EarnedBur"]
      self.EarnedSub:int = obj["EarnedSub"]
      self.EarnedMtlBur:int = obj["EarnedMtlBur"]
      self.EstBurHrs:int = obj["EstBurHrs"]
      self.EstLbrHrs:int = obj["EstLbrHrs"]
      self.ActBurHrs:int = obj["ActBurHrs"]
      self.ActLbrHrs:int = obj["ActLbrHrs"]
      self.EarBurHrs:int = obj["EarBurHrs"]
      self.EarLbrHrs:int = obj["EarLbrHrs"]
      self.QuoMtl:int = obj["QuoMtl"]
      self.QuoLbr:int = obj["QuoLbr"]
      self.QuoBur:int = obj["QuoBur"]
      self.QuoSub:int = obj["QuoSub"]
      self.QuoMtlBur:int = obj["QuoMtlBur"]
      self.QuoBurHrs:int = obj["QuoBurHrs"]
      self.QuoLbrHrs:int = obj["QuoLbrHrs"]
      self.QuotTot:int = obj["QuotTot"]
      self.EstTot:int = obj["EstTot"]
      self.ActTot:int = obj["ActTot"]
      self.EarnedTot:int = obj["EarnedTot"]
      self.ActODC:int = obj["ActODC"]
      """  Actual Other Direct Costs  """  
      self.EarnedODC:int = obj["EarnedODC"]
      """  Actual Other Direct Cost Burden  """  
      self.EstODC:int = obj["EstODC"]
      """  Estimated Other Direct Cost  """  
      self.QuoODC:int = obj["QuoODC"]
      """  Quoted Other Direct cost  """  
      self.QuoHrsTot:int = obj["QuoHrsTot"]
      self.ActHrsTot:int = obj["ActHrsTot"]
      self.EarHrsTot:int = obj["EarHrsTot"]
      self.EstHrsTot:int = obj["EstHrsTot"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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

class ProjectCostsHours_input:
   """ Required : 
   curProjectID
   """  
   def __init__(self, obj):
      self.curProjectID:str = obj["curProjectID"]
      """  Project ID  """  
      pass

class ProjectCostsHours_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjSummaryTableset] = obj["returnObj"]
      pass

