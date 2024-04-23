import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MinMaxSfyMassUpdSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetHistoryWindow(epicorHeaders = None):
   """  
   Summary: Invoke method GetHistoryWindow
   Description: This method is used to get the History Window ONLY. It will not calculate any other value.
This is used mostly for BLTester to compare results.
   OperationID: GetHistoryWindow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHistoryWindow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetSingleHistoryWindow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSingleHistoryWindow
   OperationID: GetSingleHistoryWindow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSingleHistoryWindow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSingleHistoryWindow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMinMaxSafetyRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMinMaxSafetyRecords
   OperationID: GetMinMaxSafetyRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMinMaxSafetyRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMinMaxSafetyRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateSelected
   OperationID: CalculateSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassUpdate
   OperationID: MassUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMinMaxSafetyValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMinMaxSafetyValues
   OperationID: ValidateMinMaxSafetyValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMinMaxSafetyValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMinMaxSafetyValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MinMaxSfyMassUpdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CalculateSelected_input:
   """ Required : 
   ds
   cutOffDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MinMaxSfyMassUpdTableset] = obj["ds"]
      self.cutOffDate:str = obj["cutOffDate"]
      pass

class CalculateSelected_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MinMaxSfyMassUpdTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_MinMaxSfyMassUpdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ClassID:str = obj["ClassID"]
      """  The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.  """  
      self.CalcMMSInclude:bool = obj["CalcMMSInclude"]
      """  Calculated Field of MMSInclude. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.CalcMMSSales:bool = obj["CalcMMSSales"]
      """  Calculated Field of MMSSales. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.CalcMMSIssue:bool = obj["CalcMMSIssue"]
      """  Calculated Field of MMSIssue. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.CalcMMSHistory:int = obj["CalcMMSHistory"]
      """  Calculated Field of MMSHistory. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.SaleQty:int = obj["SaleQty"]
      """  Sum of all TranQty from PartTran STK-CUS records for a specific Company/Site/Part  """  
      self.IssueQty:int = obj["IssueQty"]
      """  Sum of all TranQty from PartTran STK-MTL records for a specific Company/Site/Part  """  
      self.TotalUsage:int = obj["TotalUsage"]
      """   if CalcMMSSales and CalcMMSIssue then SaleQty + IssueQty
if CalcMMSSales  then SaleQty
if CalcMMSIssue then IssueQty  """  
      self.Select:bool = obj["Select"]
      """  External field used to select a row for Update or Mass Update  """  
      self.ClassDesc:str = obj["ClassDesc"]
      """  Full description of the part class.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.ReOrderLevel:bool = obj["ReOrderLevel"]
      """  Same as PartPlant.ReOrderLevel  """  
      self.CalcLeadTime:int = obj["CalcLeadTime"]
      """  Calculated Field of LeadTime. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. Same as PartPlant.MinimumQty. Used for Mass Update.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. Same as PartPlant.MaximumQty  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """  Safety quantity is a "purchasing cushion" limit. Same as PartPlant.SafetyQty  """  
      self.ProposedMin:int = obj["ProposedMin"]
      """  It will be calculated as DailyUsage * CalcLeadTime  """  
      self.ProposedMax:int = obj["ProposedMax"]
      """  It will be calculated as (ProposedMin * CalcMMSMaxFactor) + ProposedSafety  """  
      self.ProposedSafety:int = obj["ProposedSafety"]
      """  It will be calculated as if(CalcMMSSafetyFactor > 0) then ProposedMin * CalcMMSSafetyFactor / 100 else 0  """  
      self.CurrSafetyValue:int = obj["CurrSafetyValue"]
      """  It will be calculated as SafetyQty * PartCost  """  
      self.NewSafetyValue:int = obj["NewSafetyValue"]
      """  It will be calculated as ProposedSafety * PartCost  """  
      self.SafetyCostChange:int = obj["SafetyCostChange"]
      """  it will be calculated as NewSafetyValue - CurrSafetyValue  """  
      self.CurrMinValue:int = obj["CurrMinValue"]
      """  It will be calculated as MinimumQty * PartCost  """  
      self.CurrMaxValue:int = obj["CurrMaxValue"]
      """  It will be calculated as MaximumQty * PartCost  """  
      self.NewMinValue:int = obj["NewMinValue"]
      """  It will be calculated as ProposedMin * PartCost  """  
      self.NewMaxValue:int = obj["NewMaxValue"]
      """  It will be calculated as ProposedMax * PartCost  """  
      self.MinCostChange:int = obj["MinCostChange"]
      """  It will be calculated as NewMinValue - CurrMinValue  """  
      self.MaxCostChange:int = obj["MaxCostChange"]
      """  It will be calculated as NewMaxValue - CurrMaxValue  """  
      self.CalcMMSSafetyFactor:int = obj["CalcMMSSafetyFactor"]
      """  Calculated Field of MMSSafetyFactor. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.CalcMMSMaxFactor:int = obj["CalcMMSMaxFactor"]
      """  Calculated Field of MMSMaxFactor. It will contains the value, first from PartPlant, but if zero then it will have the value from PartClass.  """  
      self.DailyUsage:int = obj["DailyUsage"]
      """  It will be calculated as if(CalcLeadTime = 0 and TotalUsage <= 0) then 0 else TotalUsage / CalcMMSHistory  """  
      self.CostMethod:str = obj["CostMethod"]
      self.CostID:str = obj["CostID"]
      self.PartCost:int = obj["PartCost"]
      self.PartLeadTime:int = obj["PartLeadTime"]
      """  Contains the value from PartPlant.LeadTime. Used for Mass Update option.  """  
      self.CurrMinimumQty:int = obj["CurrMinimumQty"]
      """  A readonly column that contains PartPlant.MinimumQty value. Used for reference ONLY when user is working with Mass Update option.  """  
      self.CurrMaximumQty:int = obj["CurrMaximumQty"]
      """  A readonly column that contains PartPlant.MaximumQty value. Used for reference ONLY when user is working with Mass Update option.  """  
      self.CurrSafetyQty:int = obj["CurrSafetyQty"]
      """  A readonly column that contains PartPlant.SafetyQty value. Used for reference ONLY when user is working with Mass Update option.  """  
      self.CalculatedUsageQty:int = obj["CalculatedUsageQty"]
      """  Value from PartPlant.SavedCalculatedUsageQty.  """  
      self.LastUpdate:str = obj["LastUpdate"]
      """  Value from PartPlant.SavedOnDateTime  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MinMaxSfyMassUpdTableset:
   def __init__(self, obj):
      self.MinMaxSfyMassUpd:list[Erp_Tablesets_MinMaxSfyMassUpdRow] = obj["MinMaxSfyMassUpd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetHistoryWindow_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MinMaxSfyMassUpdTableset] = obj["returnObj"]
      pass

class GetMinMaxSafetyRecords_input:
   """ Required : 
   classFilter
   partFilter
   """  
   def __init__(self, obj):
      self.classFilter:str = obj["classFilter"]
      self.partFilter:str = obj["partFilter"]
      pass

class GetMinMaxSafetyRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MinMaxSfyMassUpdTableset] = obj["returnObj"]
      pass

class GetSingleHistoryWindow_input:
   """ Required : 
   partNum
   historyWindow
   cutOffDate
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.historyWindow:int = obj["historyWindow"]
      self.cutOffDate:str = obj["cutOffDate"]
      pass

class GetSingleHistoryWindow_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MinMaxSfyMassUpdTableset] = obj["returnObj"]
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

class MassUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MinMaxSfyMassUpdTableset] = obj["ds"]
      pass

class MassUpdate_output:
   def __init__(self, obj):
      pass

class ValidateMinMaxSafetyValues_input:
   """ Required : 
   minQty
   maxQty
   sfyQty
   reOrder
   """  
   def __init__(self, obj):
      self.minQty:int = obj["minQty"]
      self.maxQty:int = obj["maxQty"]
      self.sfyQty:int = obj["sfyQty"]
      self.reOrder:bool = obj["reOrder"]
      pass

class ValidateMinMaxSafetyValues_output:
   def __init__(self, obj):
      pass

