import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ChangeImpactSvc
# Description: This object is used to view the effects on each department
           that result from changes made to the schedule. This include the actual
           number of hours and days, what-if hours and days and change hours and
           days overdue. This is a non-standard bl object with no standard methods,
           it can't be updated nor deleted. This is just for information purposes.
           bo/ChangeImpact/ChangeImpact.p
           Change Impact Informer Business Object
           Fernanda Garcia
           04/28/2005
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetData(epicorHeaders = None):
   """  
   Summary: Invoke method GetData
   Description: Loads the start up data for Change Impact Informer
If a change is made to this method the same change should be applied to
the GetSpecificBinSearch method.
   OperationID: GetData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeParameters
   Description: This method will recalculate the Early/Late/OnTime jobs when the JobReq,
EarlyGracePeriod and LateGracePeriod change.
   OperationID: OnChangeParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ChangeImpactSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ChangeImpactTableset:
   def __init__(self, obj):
      self.ChgImpHed:list[Erp_Tablesets_ChgImpHedRow] = obj["ChgImpHed"]
      self.ChgImpDtl:list[Erp_Tablesets_ChgImpDtlRow] = obj["ChgImpDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ChgImpDtlRow:
   def __init__(self, obj):
      self.DeptCode:str = obj["DeptCode"]
      """  Work Center JCDepartment Code.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.HoursOver:int = obj["HoursOver"]
      """  Hours Over  """  
      self.DaysOver:int = obj["DaysOver"]
      """  Days Over  """  
      self.WIHoursOver:int = obj["WIHoursOver"]
      """  What If Hours Over  """  
      self.WIDaysOver:int = obj["WIDaysOver"]
      """  What if Days Over  """  
      self.ChgHoursOver:int = obj["ChgHoursOver"]
      """  Change Hours Over  """  
      self.ChgDaysOver:int = obj["ChgDaysOver"]
      """  Change Days Over  """  
      self.ResourceGrpIDDescription:str = obj["ResourceGrpIDDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.DeptCodeDescription:str = obj["DeptCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ChgImpHedRow:
   def __init__(self, obj):
      self.JobReq:str = obj["JobReq"]
      """  The date that is the basis for early and late calculations  """  
      self.EarlyGracePeriod:int = obj["EarlyGracePeriod"]
      """  Number of days before the JobReq Date that a job is considered early.  """  
      self.LateGracePeriod:int = obj["LateGracePeriod"]
      """  Number of day after the JobReq date that a job can be considered early  """  
      self.ActualJobsEarly:int = obj["ActualJobsEarly"]
      """  Actual Jobs Early  """  
      self.ActualJobsLate:int = obj["ActualJobsLate"]
      """  Actual Jobs Late  """  
      self.ActualJobsOntime:int = obj["ActualJobsOntime"]
      """  Actual Jobs Ontime  """  
      self.WIJobsEarly:int = obj["WIJobsEarly"]
      """  What IF Jobs Early  """  
      self.WIJobsLate:int = obj["WIJobsLate"]
      """  What If Jobs Late  """  
      self.WIJobsOnTime:int = obj["WIJobsOnTime"]
      """  What if Jobs On Time  """  
      self.ChgJobsEarly:int = obj["ChgJobsEarly"]
      """  Change Jobs Early  """  
      self.ChgJobsLate:int = obj["ChgJobsLate"]
      """  Change Jobs Late  """  
      self.ChgJobsOnTime:int = obj["ChgJobsOnTime"]
      """  Change Jobs OnTime  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ChangeImpactTableset] = obj["returnObj"]
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

class OnChangeParameters_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ChangeImpactTableset] = obj["ds"]
      pass

class OnChangeParameters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChangeImpactTableset] = obj["ds"]
      pass

      """  output parameters  """  

