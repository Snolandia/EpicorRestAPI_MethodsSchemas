import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MobileSettingsSvc
# Description: Mobile Settings Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeCompanyAndPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCompanyAndPlant
   Description: Change the company and plant for the current user
   OperationID: ChangeCompanyAndPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCompanyAndPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCompanyAndPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanyAndPlantForUser(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanyAndPlantForUser
   Description: Get list of Companies and Plants for the current user
   OperationID: GetCompanyAndPlantForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanyAndPlantForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_UserSettings(epicorHeaders = None):
   """  
   Summary: Invoke method UserSettings
   Description: Return User and Employee information
   OperationID: UserSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UserSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_validateUserForApplication(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method validateUserForApplication
   Description: Uses the current session user to validate if it is allowed to access the  application
If allowed, then message is empty, if not allowed then
the message returns the reason for which the user is not allowed to access
   OperationID: validateUserForApplication
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateUserForApplication_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateUserForApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEpicorHelpUrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEpicorHelpUrl
   Description: Wrapper around the framework ClientFunctions service to retrieve the help url.
   OperationID: GetEpicorHelpUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEpicorHelpUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEpicorHelpUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVersion(epicorHeaders = None):
   """  
   Summary: Invoke method GetVersion
   Description: Returns the BO Version
   OperationID: GetVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileSettingsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCompanyAndPlant_input:
   """ Required : 
   company
   plantID
   applicationName
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Company ID to which we want to change the users default  """  
      self.plantID:str = obj["plantID"]
      """  Site ID to which we want to change the users default  """  
      self.applicationName:str = obj["applicationName"]
      """  Application Name, Options: ERPExpense or ERPTime  """  
      pass

class ChangeCompanyAndPlant_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MobileSettingsLicenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Enable:bool = obj["Enable"]
      """  Describes whether the license is enable or not for the company  """  
      self.LicenseName:str = obj["LicenseName"]
      """  License Name  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileSettingsSessionRow:
   def __init__(self, obj):
      self.CompanyID:str = obj["CompanyID"]
      self.CompanyName:str = obj["CompanyName"]
      self.EmployeeID:str = obj["EmployeeID"]
      self.UserID:str = obj["UserID"]
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      """  Indicates if the current user is restricted to entering time against employees where their username is set in the Employee record.  """  
      self.TimeDisableCreate:bool = obj["TimeDisableCreate"]
      """  Indicates whether the user is allowed to create a Time transaction in Time Mobile application  for another employee for which they are an Approver.  """  
      self.TimeEntryAllowed:bool = obj["TimeEntryAllowed"]
      """  This value will be true if the Employee is allowed to enter Time  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      """  Indicates if the current user is restricted to entering expense against employees where their username is set in the Employee record.  """  
      self.ExpenseDisableCreate:bool = obj["ExpenseDisableCreate"]
      """  Indicates whether the user is allowed to create a Expense transaction in Expense Mobile application  for another employee for which they are an Approver.  """  
      self.ExpenseEntryAllowed:bool = obj["ExpenseEntryAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense.  """  
      self.Plant:str = obj["Plant"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.EmployeeName:str = obj["EmployeeName"]
      """  Employee Name  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  User email address  """  
      self.UserName:str = obj["UserName"]
      """  Users name  """  
      self.LangNameID:str = obj["LangNameID"]
      self.LangNameDescription:str = obj["LangNameDescription"]
      """  Language Name Description  """  
      self.LangNameCulture:str = obj["LangNameCulture"]
      """  Culture flag  """  
      self.FormatCulture:str = obj["FormatCulture"]
      self.ServerVersion:str = obj["ServerVersion"]
      """  Returns the installed Sever version to which we are connecting.  """  
      self.TimeZoneOffset:int = obj["TimeZoneOffset"]
      """  The time zone offset in seconds between UTC and the time based on the time zone defined against the company  """  
      self.IsMultiTenant:bool = obj["IsMultiTenant"]
      self.TimeAllowJobsEntry:bool = obj["TimeAllowJobsEntry"]
      """   To validate if the user can enter Production/Service time.
This validation works together with the ProjectBilling license.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileSettingsTableset:
   def __init__(self, obj):
      self.MobileSettingsSession:list[Erp_Tablesets_MobileSettingsSessionRow] = obj["MobileSettingsSession"]
      self.MobileSettingsLicense:list[Erp_Tablesets_MobileSettingsLicenseRow] = obj["MobileSettingsLicense"]
      self.MobileUserCompany:list[Erp_Tablesets_MobileUserCompanyRow] = obj["MobileUserCompany"]
      self.MobileUserPlant:list[Erp_Tablesets_MobileUserPlantRow] = obj["MobileUserPlant"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MobileUserCompanyRow:
   def __init__(self, obj):
      self.CompanyID:str = obj["CompanyID"]
      """  Company ID  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MobileUserPlantRow:
   def __init__(self, obj):
      self.CompanyID:str = obj["CompanyID"]
      """  Company ID  """  
      self.Plant:str = obj["Plant"]
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetCompanyAndPlantForUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileSettingsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetEpicorHelpUrl_input:
   """ Required : 
   label
   helpTopic
   username
   useremail
   aryTags
   zdSubDomain
   locale
   """  
   def __init__(self, obj):
      self.label:str = obj["label"]
      """  Corresponds to Label used in Zendesk for an article, and used to locate the URL of an article. Should be lowercase without spaces. In the case of Kinetic forms, use page title as label (lowercasing and trimming spaces)  """  
      self.helpTopic:str = obj["helpTopic"]
      """  The fully qualified URL of a Zendesk article. Example- 'https://epicorerp.zendesk.com/hc/en-us/articles/360022072552-View-Schedule' If using label (preferred technique) send null for helpTopic.  """  
      self.username:str = obj["username"]
      """  Consult with Epicor University writer on the generic user or users that may be appropriate. Until Epicor Idp is used, most apps will use a single user for the whole app.
            Example- 'Epicor TimeExpenseUser'  """  
      self.useremail:str = obj["useremail"]
      """  Email for user. Until actual users are passed (afer Idp), email is just meeting a Zendesk requirement and will not be used (but must consistent for user from call to call).
            Example-'erptimeexpense@epicor.com'  """  
      self.aryTags:str = obj["aryTags"]
      """  Tags are used in Zendesk to show or hide (segment) content. Consult with Epicor University writer on appropriate tags for user.
            Tags sent with call replace previous tag set. Example- ['erptime', 'erpexpense']  """  
      self.zdSubDomain:str = obj["zdSubDomain"]
      """  Consult with EU writer on the Zendesk subdomain to use  """  
      self.locale:str = obj["locale"]
      """  Set to locale of user session. For example - en-us  """  
      pass

class GetEpicorHelpUrl_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A URL with Zendesk SSO token and redirect url as querystring.  """  
      pass

class GetVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class UserSettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MobileSettingsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class validateUserForApplication_input:
   """ Required : 
   applicationName
   """  
   def __init__(self, obj):
      self.applicationName:str = obj["applicationName"]
      """  Application Name, Options: ERPExpense or ERPTime  """  
      pass

class validateUserForApplication_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

