import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CompanyLicenseInfoSvc
# Description: Return licensing data for installation id.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanyLicenseInfoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CompanyLicenseInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetLicense(epicorHeaders = None):
   """  
   Summary: Invoke method GetLicense
   Description: Return licensing dataset for the company/installation id
   OperationID: GetLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CompanyLicenseInfoSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_CSFModulesDataRow:
   def __init__(self, obj):
      self.CGCCode:str = obj["CGCCode"]
      self.CGCName:str = obj["CGCName"]
      self.Enabled:bool = obj["Enabled"]
      self.Licensed:bool = obj["Licensed"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CompanyLicenseInfoTableset:
   def __init__(self, obj):
      self.CSFModulesData:list[Erp_Tablesets_CSFModulesDataRow] = obj["CSFModulesData"]
      self.LicenseModulesData:list[Erp_Tablesets_LicenseModulesDataRow] = obj["LicenseModulesData"]
      self.UserLicenseData:list[Erp_Tablesets_UserLicenseDataRow] = obj["UserLicenseData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LicenseModulesDataRow:
   def __init__(self, obj):
      self.Enabled:bool = obj["Enabled"]
      self.Licensed:bool = obj["Licensed"]
      self.ModuleCode:str = obj["ModuleCode"]
      self.ModuleName:str = obj["ModuleName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserLicenseDataRow:
   def __init__(self, obj):
      self.ActiveUsers:int = obj["ActiveUsers"]
      self.AvailableUsers:int = obj["AvailableUsers"]
      self.MaxUsers:int = obj["MaxUsers"]
      self.SysRowID:str = obj["SysRowID"]
      self.UserLicenseCode:str = obj["UserLicenseCode"]
      self.UserLicenseName:str = obj["UserLicenseName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetLicense_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CompanyLicenseInfoTableset] = obj["returnObj"]
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

