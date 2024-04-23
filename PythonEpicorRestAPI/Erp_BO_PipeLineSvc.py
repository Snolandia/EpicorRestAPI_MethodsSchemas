import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PipeLineSvc
# Description: PipeLineSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BuildPipeLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildPipeLine
   Description: Call this method to build the Pipeline grid for a Salesperson.
   OperationID: BuildPipeLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildPipeLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildPipeLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CompanyActualQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CompanyActualQuota
   Description: Company Actual Quota.
   OperationID: CompanyActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CompanyActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetActuals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetActuals
   Description: Call the correct method to retrieve Actuals data based on the Actuals Type.
   OperationID: GetActuals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetActuals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetActuals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetComboValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetComboValues
   Description: Call this method to get list of Region, Territory and Sales Rep
There are three levels of access:
View All: This is enabled when the user's SalesRepID has 'View Company Pipeline' turned on in
Workforce Maintenance.
Can view aggregate totals of Actuals by Company, Region, Territory or SalesRep for ALL
regions, territories, salesreps in the company
Sales Manager:  This is enabled when the user's SalesRepID is entered as the Sales Manager for one
or more Regions in Sales Region Maintenance.
Can view aggregate totals of Actuals by Region, Territory or SalesRep for the
regions for which they are Sales Manager
In this situation:
pcTypeList contains Region, Territory, SalesManager and SalesRep
pcRegionList contains the Regions for which the current user is Sales Manager
pcTerritoryList contains the territories for their Regions
pcSalesRepList contains only the SalesReps that "Report To" the current user
Sales Rep:  This is the level of access granted when neither of the other two levels apply.
Can view only their own totals, and NOT aggregated by Region, or Territory
In this situation:
pcTypeList contains only the "SalesRep" choice
pcRegionList and pcTerritoryList are empty
pcSalesRepList contains only the SalesRep associated with the current user
   OperationID: GetComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetComboValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComboValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDates(epicorHeaders = None):
   """  
   Summary: Invoke method GetDates
   OperationID: GetDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetQuarter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuarter
   Description: This method returns the Fiscal Quarter for given Company and FiscalPeriod.
   OperationID: GetQuarter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuarter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuarter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTypeList
   Description: Call this method to get list of Region, Territory and Sales Rep
There are three levels of access:
View All: This is enabled when the user's SalesRepID has 'View Company Pipeline' turned on in
Workforce Maintenance.
Can view aggregate totals of Actuals by Company, Region, Territory or SalesRep for ALL
regions, territories, salesreps in the company
Sales Manager:  This is enabled when the user's SalesRepID is entered as the Sales Manager for one
or more Regions in Sales Region Maintenance.
Can view aggregate totals of Actuals by Region, Territory or SalesRep for the
regions for which they are Sales Manager
In this situation:
pcTypeList contains Region, Territory, SalesManager and SalesRep
pcRegionList contains the Regions for which the current user is Sales Manager
pcTerritoryList contains the territories for their Regions
pcSalesRepList contains only the SalesReps that "Report To" the current user
Sales Rep:  This is the level of access granted when neither of the other two levels apply.
Can view only their own totals, and NOT aggregated by Region, or Territory
In this situation:
pcTypeList contains only the "SalesRep" choice
pcRegionList and pcTerritoryList are empty
pcSalesRepList contains only the SalesRep associated with the current user
   OperationID: GetTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetComboValuesDataset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetComboValuesDataset
   Description: Get the valid region, territory, and sales rep values and populate them in the combo boxes.
   OperationID: GetComboValuesDataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetComboValuesDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComboValuesDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegionActualQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegionActualQuota
   Description: This method displays the Regional Actual Quota
   OperationID: RegionActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegionActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegionActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SalesManagerActualQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SalesManagerActualQuota
   Description: This method displays Sales Manager Actual Quota.
   OperationID: SalesManagerActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesManagerActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesManagerActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SalesRepActualQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SalesRepActualQuota
   Description: This method displays Sales Rep's Actual Quota.
   OperationID: SalesRepActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesRepActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesRepActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetupPipeLineControlTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetupPipeLineControlTable
   Description: Initialize the PipeLineControl table.
   OperationID: SetupPipeLineControlTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetupPipeLineControlTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetupPipeLineControlTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TerritoryActualQuota(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TerritoryActualQuota
   Description: This method displays Territory Actual Quota
   OperationID: TerritoryActualQuota
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TerritoryActualQuota_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TerritoryActualQuota_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PipeLineSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildPipeLine_input:
   """ Required : 
   pdtFromFilterDate
   pdtToFilterDate
   piFiscalYear
   piFiscalPeriod
   """  
   def __init__(self, obj):
      self.pdtFromFilterDate:str = obj["pdtFromFilterDate"]
      """  From Filter Date  """  
      self.pdtToFilterDate:str = obj["pdtToFilterDate"]
      """  To Filter Date  """  
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      pass

class BuildPipeLine_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PipeLineTableset] = obj["returnObj"]
      pass

class CompanyActualQuota_input:
   """ Required : 
   piFiscalYear
   pcFiscalYearSuffix
   piFiscalPeriod
   pdtFromFilterDate
   pdtToFilterDate
   ds
   """  
   def __init__(self, obj):
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.pcFiscalYearSuffix:str = obj["pcFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      self.pdtFromFilterDate:str = obj["pdtFromFilterDate"]
      """  From Filter Date  """  
      self.pdtToFilterDate:str = obj["pdtToFilterDate"]
      """  To Filter Date  """  
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

class CompanyActualQuota_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PipeLineControlRow:
   def __init__(self, obj):
      self.AType:str = obj["AType"]
      """  Type of Actuals to show in Salesperson Pipeline  """  
      self.ATypeList:str = obj["ATypeList"]
      """  Delimited list of available Actual Types  """  
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FromDate:str = obj["FromDate"]
      self.Period:int = obj["Period"]
      self.Quarter:int = obj["Quarter"]
      self.Region:str = obj["Region"]
      self.RegionList:str = obj["RegionList"]
      """  Delimited list of regions (RegionCode`Description~RegionCode`Description)  """  
      self.SalesRep:str = obj["SalesRep"]
      self.SalesRepList:str = obj["SalesRepList"]
      """  Delimited list of available Sales Reps  """  
      self.Territory:str = obj["Territory"]
      self.TerritoryList:str = obj["TerritoryList"]
      """  Delimited list of available Territories  """  
      self.ToDate:str = obj["ToDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PipeLineGridRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company x  """  
      self.RegionCode:str = obj["RegionCode"]
      """  Region Code  """  
      self.TerritoryID:str = obj["TerritoryID"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.CustID:str = obj["CustID"]
      self.Manager:str = obj["Manager"]
      self.ExpectedClose:str = obj["ExpectedClose"]
      self.PrimeRep:bool = obj["PrimeRep"]
      self.IsConsolidated:bool = obj["IsConsolidated"]
      self.PipeLineExpected:int = obj["PipeLineExpected"]
      self.PipeLineAdjusted:int = obj["PipeLineAdjusted"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CurrentMileStoneDesc:str = obj["CurrentMileStoneDesc"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.PipeLineBestCs:int = obj["PipeLineBestCs"]
      self.PipeLineWorstCs:int = obj["PipeLineWorstCs"]
      self.SysRowID:str = obj["SysRowID"]
      self.ManagerName:str = obj["ManagerName"]
      self.RegionDescription:str = obj["RegionDescription"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PipeLineTableset:
   def __init__(self, obj):
      self.PipeLineGrid:list[Erp_Tablesets_PipeLineGridRow] = obj["PipeLineGrid"]
      self.PipeLineControl:list[Erp_Tablesets_PipeLineControlRow] = obj["PipeLineControl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PipeLineTotalsRow:
   def __init__(self, obj):
      self.MTDQuota:int = obj["MTDQuota"]
      self.MTDActual:int = obj["MTDActual"]
      self.QTDQuota:int = obj["QTDQuota"]
      self.QTDActual:int = obj["QTDActual"]
      self.YTDQuota:int = obj["YTDQuota"]
      self.YTDActual:int = obj["YTDActual"]
      self.OverDue:int = obj["OverDue"]
      self.DueToday:int = obj["DueToday"]
      self.DueThisWeek:int = obj["DueThisWeek"]
      self.DueNextWeek:int = obj["DueNextWeek"]
      self.DueThisMonth:int = obj["DueThisMonth"]
      self.DueNextMonth:int = obj["DueNextMonth"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PipeLineTotalsTableset:
   def __init__(self, obj):
      self.PipeLineTotals:list[Erp_Tablesets_PipeLineTotalsRow] = obj["PipeLineTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetActuals_input:
   """ Required : 
   actualsType
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   fromDate
   toDate
   salesRepCode
   regionCode
   territoryID
   ds
   """  
   def __init__(self, obj):
      self.actualsType:str = obj["actualsType"]
      """  Type of actuals to retrieve  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Selected fiscal year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Suffix for the fiscal year  """  
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      """  Selected fiscal period  """  
      self.fromDate:str = obj["fromDate"]
      """  Date from which we filter resultsDate from which we filter results  """  
      self.toDate:str = obj["toDate"]
      """  Date up to which we filter results  """  
      self.salesRepCode:str = obj["salesRepCode"]
      self.regionCode:str = obj["regionCode"]
      self.territoryID:str = obj["territoryID"]
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

class GetActuals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetComboValuesDataset_input:
   """ Required : 
   actualsType
   ds
   """  
   def __init__(self, obj):
      self.actualsType:str = obj["actualsType"]
      """  Type of actuals to populate  """  
      self.ds:list[Erp_Tablesets_PipeLineTableset] = obj["ds"]
      pass

class GetComboValuesDataset_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetComboValues_input:
   """ Required : 
   pcActualsType
   """  
   def __init__(self, obj):
      self.pcActualsType:str = obj["pcActualsType"]
      """  Type (aggregation-level). One of: Company, Region, Territory, SalesManager, SalesRep  """  
      pass

class GetComboValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcRegionList:str = obj["parameters"]
      self.pcTerritoryList:str = obj["parameters"]
      self.pcSalesRepList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.piFiscalYear:int = obj["parameters"]
      self.pcFiscalYearSuffix:str = obj["parameters"]
      self.piFiscalPeriod:int = obj["parameters"]
      self.pdtFromFilterDate:str = obj["parameters"]
      self.pdtToFilterDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetQuarter_input:
   """ Required : 
   piFiscalYear
   pcFiscalYearSuffix
   piFiscalPeriod
   """  
   def __init__(self, obj):
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.pcFiscalYearSuffix:str = obj["pcFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      pass

class GetQuarter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.piFiscalQtr:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcTypeList:str = obj["parameters"]
      pass

      """  output parameters  """  

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

class RegionActualQuota_input:
   """ Required : 
   pcSalesRepCode
   pcRegionCode
   piFiscalYear
   pcFiscalYearSuffix
   piFiscalPeriod
   pdtFromFilterDate
   pdtToFilterDate
   ds
   """  
   def __init__(self, obj):
      self.pcSalesRepCode:str = obj["pcSalesRepCode"]
      """  SalesRep Code  """  
      self.pcRegionCode:str = obj["pcRegionCode"]
      """  Region Code  """  
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.pcFiscalYearSuffix:str = obj["pcFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      self.pdtFromFilterDate:str = obj["pdtFromFilterDate"]
      """  From Filter Date  """  
      self.pdtToFilterDate:str = obj["pdtToFilterDate"]
      """  To Filter Date  """  
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

class RegionActualQuota_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SalesManagerActualQuota_input:
   """ Required : 
   pcSalesRepCode
   piFiscalYear
   pcFiscalYearSuffix
   piFiscalPeriod
   pdtFromFilterDate
   pdtToFilterDate
   ds
   """  
   def __init__(self, obj):
      self.pcSalesRepCode:str = obj["pcSalesRepCode"]
      """  SalesRep Code  """  
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.pcFiscalYearSuffix:str = obj["pcFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      self.pdtFromFilterDate:str = obj["pdtFromFilterDate"]
      """  From Filter Date  """  
      self.pdtToFilterDate:str = obj["pdtToFilterDate"]
      """  To Filter Date  """  
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

class SalesManagerActualQuota_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SalesRepActualQuota_input:
   """ Required : 
   pcSalesRepCode
   pcTerritoryID
   piFiscalYear
   pcFiscalYearSuffix
   piFiscalPeriod
   pdtFromFilterDate
   pdtToFilterDate
   ds
   """  
   def __init__(self, obj):
      self.pcSalesRepCode:str = obj["pcSalesRepCode"]
      """  SalesRep Code  """  
      self.pcTerritoryID:str = obj["pcTerritoryID"]
      """  Territory ID  """  
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.pcFiscalYearSuffix:str = obj["pcFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      self.pdtFromFilterDate:str = obj["pdtFromFilterDate"]
      """  From Filter Date  """  
      self.pdtToFilterDate:str = obj["pdtToFilterDate"]
      """  To Filter Date  """  
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

class SalesRepActualQuota_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetupPipeLineControlTable_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTableset] = obj["ds"]
      pass

class SetupPipeLineControlTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TerritoryActualQuota_input:
   """ Required : 
   pcSalesRepCode
   pcTerritoryID
   piFiscalYear
   pcFiscalYearSuffix
   piFiscalPeriod
   pdtFromFilterDate
   pdtToFilterDate
   ds
   """  
   def __init__(self, obj):
      self.pcSalesRepCode:str = obj["pcSalesRepCode"]
      """  SalesRep Code  """  
      self.pcTerritoryID:str = obj["pcTerritoryID"]
      """  Territory ID  """  
      self.piFiscalYear:int = obj["piFiscalYear"]
      """  Fiscal Year  """  
      self.pcFiscalYearSuffix:str = obj["pcFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.piFiscalPeriod:int = obj["piFiscalPeriod"]
      """  Fiscal Period  """  
      self.pdtFromFilterDate:str = obj["pdtFromFilterDate"]
      """  From Filter Date  """  
      self.pdtToFilterDate:str = obj["pdtToFilterDate"]
      """  To Filter Date  """  
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

class TerritoryActualQuota_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PipeLineTotalsTableset] = obj["ds"]
      pass

      """  output parameters  """  

