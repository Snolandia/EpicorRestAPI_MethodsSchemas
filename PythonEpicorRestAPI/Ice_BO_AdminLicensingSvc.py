import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.AdminLicensingSvc
# Description: License maintenance business object for use by Admin Console
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetLicense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLicense
   Description: Retrieving licensing information for the installation
   OperationID: GetLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SysLicenseExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SysLicenseExists
   Description: Checks for existance of SysLicense record
   OperationID: SysLicenseExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SysLicenseExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SysLicenseExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLicense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLicense
   Description: This method deletes the License with the specified installation id.
   OperationID: DeleteLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExistingLicense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExistingLicense
   Description: Updates a license file if an update is available.
   OperationID: UpdateExistingLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExistingLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExistingLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableModule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableModule
   Description: This method enables a licensed feature/module.
   OperationID: EnableModule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableModule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableModule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableSingleModule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableSingleModule
   Description: Enables a license module.
   OperationID: EnableSingleModule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableSingleModule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSingleModule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLicenseList(epicorHeaders = None):
   """  
   Summary: Invoke method GetLicenseList
   Description: Returns a list of all licenses.
   OperationID: GetLicenseList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicenseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetUsableLicenseList(epicorHeaders = None):
   """  
   Summary: Invoke method GetUsableLicenseList
   Description: Returns a list of all usable licenses.
   OperationID: GetUsableLicenseList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUsableLicenseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ImportLicense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportLicense
   Description: This method imports a new License.
   OperationID: ImportLicense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportLicense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportLicense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAndDownloadCloudLicenseUpdates(epicorHeaders = None):
   """  
   Summary: Invoke method CheckAndDownloadCloudLicenseUpdates
   Description: Checks the Global license server and download cloud license updates if exists.
   OperationID: CheckAndDownloadCloudLicenseUpdates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAndDownloadCloudLicenseUpdates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetTenantID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetTenantID
   Description: Sets the tenant ID by updated or creating the row in LicenseTenant
   OperationID: SetTenantID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetTenantID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLicensesByTenantID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLicensesByTenantID
   Description: Gets the licenses by tenant ID.
   OperationID: GetLicensesByTenantID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLicensesByTenantID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicensesByTenantID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSysLicenseList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSysLicenseList
   OperationID: GetSysLicenseList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSysLicenseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.AdminLicensingSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckAndDownloadCloudLicenseUpdates_output:
   def __init__(self, obj):
      pass

class DeleteLicense_input:
   """ Required : 
   installationId
   """  
   def __init__(self, obj):
      self.installationId:str = obj["installationId"]
      """  Installation id of license to be deleted  """  
      pass

class DeleteLicense_output:
   def __init__(self, obj):
      pass

class EnableModule_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_AdminLicensingTableset] = obj["ds"]
      pass

class EnableModule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_AdminLicensingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EnableSingleModule_input:
   """ Required : 
   installationId
   moduleId
   """  
   def __init__(self, obj):
      self.installationId:str = obj["installationId"]
      """  The installation identifier.  """  
      self.moduleId:str = obj["moduleId"]
      """  The module identifier.  """  
      pass

class EnableSingleModule_output:
   def __init__(self, obj):
      pass

class GetLicenseList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminLicensingTableset] = obj["returnObj"]
      pass

class GetLicense_input:
   """ Required : 
   installationId
   """  
   def __init__(self, obj):
      self.installationId:str = obj["installationId"]
      pass

class GetLicense_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminLicensingTableset] = obj["returnObj"]
      pass

class GetLicensesByTenantID_input:
   """ Required : 
   tenantID
   """  
   def __init__(self, obj):
      self.tenantID:str = obj["tenantID"]
      """  The tenant ID.  """  
      pass

class GetLicensesByTenantID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminSerialNumberListTableset] = obj["returnObj"]
      pass

class GetSysLicenseList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysLicenseTableset] = obj["returnObj"]
      pass

class GetUsableLicenseList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AdminSerialNumberListTableset] = obj["returnObj"]
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

class Ice_Tablesets_AdminCSFLicenseRow:
   def __init__(self, obj):
      self.Enabled:bool = obj["Enabled"]
      self.Licensed:bool = obj["Licensed"]
      self.CGCCode:str = obj["CGCCode"]
      self.CGCName:str = obj["CGCName"]
      self.CountryGroup:bool = obj["CountryGroup"]
      self.CGID:str = obj["CGID"]
      self.InstallationID:str = obj["InstallationID"]
      """  Uniqueidentifier provided by the license file.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminLicensingTableset:
   def __init__(self, obj):
      self.AdminSerialNumber:list[Ice_Tablesets_AdminSerialNumberRow] = obj["AdminSerialNumber"]
      self.AdminCSFLicense:list[Ice_Tablesets_AdminCSFLicenseRow] = obj["AdminCSFLicense"]
      self.AdminModuleLicense:list[Ice_Tablesets_AdminModuleLicenseRow] = obj["AdminModuleLicense"]
      self.AdminUserLicense:list[Ice_Tablesets_AdminUserLicenseRow] = obj["AdminUserLicense"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AdminModuleLicenseRow:
   def __init__(self, obj):
      self.Enabled:bool = obj["Enabled"]
      self.Licensed:bool = obj["Licensed"]
      self.ModuleCode:str = obj["ModuleCode"]
      self.ModuleName:str = obj["ModuleName"]
      self.Automatic:bool = obj["Automatic"]
      self.InstallationID:str = obj["InstallationID"]
      """  Uniqueidentifier provided by the license file.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminSerialNumberListRow:
   def __init__(self, obj):
      self.MaxUsers:int = obj["MaxUsers"]
      self.EvalExpires:str = obj["EvalExpires"]
      self.MaxAdditionalDCUsers:int = obj["MaxAdditionalDCUsers"]
      self.DBLevel:int = obj["DBLevel"]
      self.DBPatchLevel:str = obj["DBPatchLevel"]
      self.MaxAdditionalDCRMUsers:int = obj["MaxAdditionalDCRMUsers"]
      """  Disconnected CRM Salesperson User Limit  """  
      self.MaxAdditionalDCRMSEUsers:int = obj["MaxAdditionalDCRMSEUsers"]
      """  Disconnected CRM Sales Engineer User Limit  """  
      self.MaxWebServices:int = obj["MaxWebServices"]
      self.Multitenant:bool = obj["Multitenant"]
      """  An Isolated Company (=True) license indicates that this company is a Single Company in a shared (Hosted)database and should not be able to affect changes or share any data or administrative functions with other companies in the system.  """  
      self.Version:str = obj["Version"]
      """  A uniqueidentifier provided by the license file.  """  
      self.Edition:str = obj["Edition"]
      self.AssignedCompanies:str = obj["AssignedCompanies"]
      self.Product:str = obj["Product"]
      self.MaxAdditionalSCUsers:int = obj["MaxAdditionalSCUsers"]
      self.MaxAdditionalCCUsers:int = obj["MaxAdditionalCCUsers"]
      self.MaxAdditionalCRMUsers:int = obj["MaxAdditionalCRMUsers"]
      self.MaxAdditionalMFWUsers:int = obj["MaxAdditionalMFWUsers"]
      self.MaxAdditionalTEUsers:int = obj["MaxAdditionalTEUsers"]
      self.TenantID:str = obj["TenantID"]
      """  Holds the tenant identity all companies using this license will operate under.  """  
      self.InstallationID:str = obj["InstallationID"]
      self.UpdateAvailable:bool = obj["UpdateAvailable"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminSerialNumberListTableset:
   def __init__(self, obj):
      self.AdminSerialNumberList:list[Ice_Tablesets_AdminSerialNumberListRow] = obj["AdminSerialNumberList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_AdminSerialNumberRow:
   def __init__(self, obj):
      self.MaxUsers:int = obj["MaxUsers"]
      self.EvalExpires:str = obj["EvalExpires"]
      self.MaxAdditionalDCUsers:int = obj["MaxAdditionalDCUsers"]
      self.DBLevel:int = obj["DBLevel"]
      self.DBPatchLevel:str = obj["DBPatchLevel"]
      self.MaxAdditionalDCRMUsers:int = obj["MaxAdditionalDCRMUsers"]
      """  Disconnected CRM Salesperson User Limit  """  
      self.MaxAdditionalDCRMSEUsers:int = obj["MaxAdditionalDCRMSEUsers"]
      """  Disconnected CRM Sales Engineer User Limit  """  
      self.MaxWebServices:int = obj["MaxWebServices"]
      self.Multitenant:bool = obj["Multitenant"]
      """  An Isolated Company (=True) license indicates that this company is a Single Company in a shared (Hosted)database and should not be able to affect changes or share any data or administrative functions with other companies in the system.  """  
      self.Version:str = obj["Version"]
      self.Edition:str = obj["Edition"]
      self.AssignedCompanies:str = obj["AssignedCompanies"]
      self.Product:str = obj["Product"]
      self.MaxAdditionalSCUsers:int = obj["MaxAdditionalSCUsers"]
      self.MaxAdditionalCCUsers:int = obj["MaxAdditionalCCUsers"]
      self.MaxAdditionalCRMUsers:int = obj["MaxAdditionalCRMUsers"]
      self.MaxAdditionalMFWUsers:int = obj["MaxAdditionalMFWUsers"]
      self.MaxAdditionalTEUsers:int = obj["MaxAdditionalTEUsers"]
      self.InstallationID:str = obj["InstallationID"]
      """  Uniqueidentifier provided by the license file.  """  
      self.TenantID:str = obj["TenantID"]
      """  Holds the tenant identity all companies using this license will operate under.  """  
      self.UpdateAvailable:bool = obj["UpdateAvailable"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AdminUserLicenseRow:
   def __init__(self, obj):
      self.ActiveUsers:int = obj["ActiveUsers"]
      self.AvailableUsers:int = obj["AvailableUsers"]
      self.MaxUsers:int = obj["MaxUsers"]
      self.UserLicenseCode:str = obj["UserLicenseCode"]
      self.UserLicenseName:str = obj["UserLicenseName"]
      self.InstallationID:str = obj["InstallationID"]
      """  Uniqueidentifier provided by the license file.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysLicenseRow:
   def __init__(self, obj):
      self.InstallationID:str = obj["InstallationID"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysLicenseTableset:
   def __init__(self, obj):
      self.SysLicense:list[Ice_Tablesets_SysLicenseRow] = obj["SysLicense"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportLicense_input:
   """ Required : 
   fileName
   licenseInfo
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  The name of the license file to import  """  
      self.licenseInfo:str = obj["licenseInfo"]
      """  Serial number and codes of license to be imported.  """  
      pass

class ImportLicense_output:
   def __init__(self, obj):
      pass

class SetTenantID_input:
   """ Required : 
   installationID
   tenantID
   """  
   def __init__(self, obj):
      self.installationID:str = obj["installationID"]
      """  The installation ID.  """  
      self.tenantID:str = obj["tenantID"]
      """  The tenant ID.  """  
      pass

class SetTenantID_output:
   def __init__(self, obj):
      pass

class SysLicenseExists_input:
   """ Required : 
   name
   """  
   def __init__(self, obj):
      self.name:str = obj["name"]
      """  The Name of the SysLicense to check  """  
      pass

class SysLicenseExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExistingLicense_input:
   """ Required : 
   installationId
   """  
   def __init__(self, obj):
      self.installationId:str = obj["installationId"]
      """  Installation id of license to be updated.  """  
      pass

class UpdateExistingLicense_output:
   def __init__(self, obj):
      pass

