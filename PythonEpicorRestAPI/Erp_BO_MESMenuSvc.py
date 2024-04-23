import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MESMenuSvc
# Description: Business object to interact with Handheld/MES Menu Security
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckMESMenuInitializedStatus(epicorHeaders = None):
   """  
   Summary: Invoke method CheckMESMenuInitializedStatus
   Description: Checks whether the current company has any MESMenu data initialized.
   OperationID: CheckMESMenuInitializedStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckMESMenuInitializedStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CheckCurrentUserSecurityMgr(epicorHeaders = None):
   """  
   Summary: Invoke method CheckCurrentUserSecurityMgr
   Description: Checks whether the current user is a security manager.
   OperationID: CheckCurrentUserSecurityMgr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCurrentUserSecurityMgr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CheckEmployeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEmployeeID
   Description: Checks whether the specified employee is a valid, active employee.
   OperationID: CheckEmployeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEmployeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckUserSiteAccess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckUserSiteAccess
   Description: Checks whether the specified user has access to the site defined in MES.
   OperationID: CheckUserSiteAccess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckUserSiteAccess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUserSiteAccess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMenuData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMenuData
   Description: Gets MESMenu data
   OperationID: GetMenuData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMenuData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMenuData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateMenuData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateMenuData
   Description: Updates MESMenu and MESMenuSecurity tables
   OperationID: UpdateMenuData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMenuData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMenuData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InitializeMESMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InitializeMESMenu
   Description: Initializes or reinitializes the MESMenu data for the current company.
   OperationID: InitializeMESMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InitializeMESMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeMESMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetEmployeeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetEmployeeID
   Description: Call to change EmployeeID if allowed by EmpBasic settings
   OperationID: SetEmployeeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetEmployeeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetEmployeeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportMESMenuData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportMESMenuData
   Description: Import MESMenu data received in a MESMenuTableset, and add it into MESMenu and MESMenuSecurity tables.
   OperationID: ImportMESMenuData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportMESMenuData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportMESMenuData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MESMenuSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckCurrentUserSecurityMgr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isSecurityMgr:bool = obj["isSecurityMgr"]
      pass

      """  output parameters  """  

class CheckEmployeeID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID to check  """  
      pass

class CheckEmployeeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sysUserID:str = obj["parameters"]
      self.empName:str = obj["parameters"]
      self.isValidActiveEmp:bool = obj["isValidActiveEmp"]
      pass

      """  output parameters  """  

class CheckMESMenuInitializedStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isInitialized:bool = obj["isInitialized"]
      pass

      """  output parameters  """  

class CheckUserSiteAccess_input:
   """ Required : 
   companyID
   userID
   newSite
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID defined in MES.  """  
      self.userID:str = obj["userID"]
      """  User ID to check  """  
      self.newSite:str = obj["newSite"]
      """  Site defined in MES.  """  
      pass

class CheckUserSiteAccess_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Returns True if the provided user ID has access to the site.  """  
      pass

class Erp_Tablesets_MESMenuRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company, if MESMenu row is generated data. For system data this is empty.  """  
      self.MESMenuID:int = obj["MESMenuID"]
      """  Unique identifier for the record  """  
      self.ParentMESMenuID:int = obj["ParentMESMenuID"]
      """  Unique identifier of the parent record. This is be the menu it will be displayed under on the Handheld MESand in the maintenance program.  """  
      self.MenuType:str = obj["MenuType"]
      """  Type of menu. H = Handheld MES / M = MES  """  
      self.Seq:int = obj["Seq"]
      """  Used to sort the items on the Handheld MES menu. Low to high.  """  
      self.MenuID:str = obj["MenuID"]
      """  The system menu IDof the menu item to invoke when the user selects this item on the menu. Blank for menus.  """  
      self.MenuDesc:str = obj["MenuDesc"]
      """  The description that appears on the Handheld MES menu and in the maintenance program.  """  
      self.Hidden:bool = obj["Hidden"]
      """  True if the item should be hidden from the Handheld MES menu.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  True if row is system data, false for data generated for specific company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MESMaterialHandler:bool = obj["MESMaterialHandler"]
      self.MESSupervisor:bool = obj["MESSupervisor"]
      self.MESShipping:bool = obj["MESShipping"]
      self.MESProduction:bool = obj["MESProduction"]
      self.MESService:bool = obj["MESService"]
      self.PCIDInbound:bool = obj["PCIDInbound"]
      self.PCIDOutbound:bool = obj["PCIDOutbound"]
      self.PCIDInventory:bool = obj["PCIDInventory"]
      self.PCIDManufacturing:bool = obj["PCIDManufacturing"]
      self.PCIDQuality:bool = obj["PCIDQuality"]
      self.CurrentEmpAllowed:bool = obj["CurrentEmpAllowed"]
      self.TranslateMenuDesc:str = obj["TranslateMenuDesc"]
      self.DisableRow:bool = obj["DisableRow"]
      """  Indicates if the row is disabled  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MESMenuSecurityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company, if MESMenu row is generated data. For system data this is empty.  """  
      self.MESMenuID:int = obj["MESMenuID"]
      """  The unique idenfiier of the MESMenu record this record pertains to  """  
      self.SecurityGroup:str = obj["SecurityGroup"]
      """  The group the role belongs to. M = Traditional MES/ P = Package Control  """  
      self.Role:str = obj["Role"]
      """  The role from a set of predefined roles that is required to access the item  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  True if row is system data, false for data generated for specific company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MESMenuTableset:
   def __init__(self, obj):
      self.MESMenu:list[Erp_Tablesets_MESMenuRow] = obj["MESMenu"]
      self.MESMenuSecurity:list[Erp_Tablesets_MESMenuSecurityRow] = obj["MESMenuSecurity"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetMenuData_input:
   """ Required : 
   empID
   menuTypes
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Empty if called from maintenance UI, currently selected employee ID if called from menus  """  
      self.menuTypes:str = obj["menuTypes"]
      """  MenuType to retrieve. Blank for all. Accepts multiple ~ delimited values.  """  
      pass

class GetMenuData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MESMenuTableset] = obj["returnObj"]
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

class ImportMESMenuData_input:
   """ Required : 
   mesMenuTS
   fullMenuList
   recreateFromSeedData
   """  
   def __init__(self, obj):
      self.mesMenuTS:list[Erp_Tablesets_MESMenuTableset] = obj["mesMenuTS"]
      self.fullMenuList:bool = obj["fullMenuList"]
      """  Indicates the type of process to run: if True, then a full dataset process. This includes deleting exsiting seed data. If False, then an incremental partial dataset process. There is no elements deletion in this case.  """  
      self.recreateFromSeedData:bool = obj["recreateFromSeedData"]
      """  Indicates if a recreation of the Menus based on the current seed data is required before the data processing. When True, then dataset is optional.  """  
      pass

class ImportMESMenuData_output:
   def __init__(self, obj):
      pass

class InitializeMESMenu_input:
   """ Required : 
   overwriteExisting
   """  
   def __init__(self, obj):
      self.overwriteExisting:bool = obj["overwriteExisting"]
      """  Set to true to overwrite existing MESMenu data.  """  
      pass

class InitializeMESMenu_output:
   def __init__(self, obj):
      pass

class SetEmployeeID_input:
   """ Required : 
   EmployeeID
   """  
   def __init__(self, obj):
      self.EmployeeID:str = obj["EmployeeID"]
      pass

class SetEmployeeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DcdUserID:str = obj["parameters"]
      self.LoginRequired:bool = obj["LoginRequired"]
      pass

      """  output parameters  """  

class UpdateMenuData_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MESMenuTableset] = obj["ds"]
      pass

class UpdateMenuData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MESMenuTableset] = obj["ds"]
      pass

      """  output parameters  """  

