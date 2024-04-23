import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MobileCRMSvc
# Description: MobileCRM main object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetCRMEnvironment(epicorHeaders = None):
   """  
   Summary: Invoke method GetCRMEnvironment
   Description: Get CRM Environment Variables
   OperationID: GetCRMEnvironment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCRMEnvironment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetCustomerIndustryCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCustomerIndustryCodes
   Description: Set customer Industry Types
   OperationID: SetCustomerIndustryCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCustomerIndustryCodes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCustomerIndustryCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetCustomerAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetCustomerAttributes
   Description: Set Customer Attributes
   OperationID: SetCustomerAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetCustomerAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetCustomerAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePerConLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePerConLink
   Description: Create PerConLnk records. Pass only the perConLnk table
   OperationID: CreatePerConLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePerConLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePerConLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MobileCRMSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CreatePerConLink_input:
   """ Required : 
   perCon
   """  
   def __init__(self, obj):
      self.perCon:list[Erp_Tablesets_CRMPerConLnkListTableset] = obj["perCon"]
      pass

class CreatePerConLink_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AttributListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrCode:str = obj["AttrCode"]
      """  Descriptive code assigned by user which uniquely identifies an attribute master record.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.AttrDescription:str = obj["AttrDescription"]
      """  Description of the attribute  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this attribute can be assigned to a customer.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AttributListTableset:
   def __init__(self, obj):
      self.AttributList:list[Erp_Tablesets_AttributListRow] = obj["AttributList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CRMEnvironmentDataTableset:
   def __init__(self, obj):
      self.CRMEnvironment:list[Erp_Tablesets_CRMEnvironmentRow] = obj["CRMEnvironment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CRMEnvironmentRow:
   def __init__(self, obj):
      self.UserID:str = obj["UserID"]
      self.ServerTime:str = obj["ServerTime"]
      """  Server local time  """  
      self.ServerUtcTime:str = obj["ServerUtcTime"]
      self.ServerUtcOffset:int = obj["ServerUtcOffset"]
      self.TenantID:str = obj["TenantID"]
      self.PatchLevel:str = obj["PatchLevel"]
      self.PatchLevelApp:str = obj["PatchLevelApp"]
      self.InstallationName:str = obj["InstallationName"]
      self.CurLangID:str = obj["CurLangID"]
      self.CountryCode:str = obj["CountryCode"]
      self.ClientDateFormat:str = obj["ClientDateFormat"]
      self.ProductName:str = obj["ProductName"]
      self.ProductCode:str = obj["ProductCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CRMPerConLnkListTableset:
   def __init__(self, obj):
      self.CRMPerConLnk:list[Erp_Tablesets_CRMPerConLnkRow] = obj["CRMPerConLnk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CRMPerConLnkRow:
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      self.ContextLink:str = obj["ContextLink"]
      self.LinkSysRowID:str = obj["LinkSysRowID"]
      self.PrimaryContext:bool = obj["PrimaryContext"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ICCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ICCode:str = obj["ICCode"]
      """  Represents the SIC/ISIC/NAICS/NACE code for the current industry class.  """  
      self.ICTypeID:str = obj["ICTypeID"]
      """  Foreign key to ICType table. A short name, acronym or identifier for the Industry Class Type.  """  
      self.Description:str = obj["Description"]
      """  Descriptive name for the Industry Class.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ICTypeDescription:str = obj["ICTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ICTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ICTypeID:str = obj["ICTypeID"]
      """  A short name, acronym or identifier for the Industry Class Type.  """  
      self.Description:str = obj["Description"]
      """  Full name or description for the Industry Class Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IndustryClassTableset:
   def __init__(self, obj):
      self.ICType:list[Erp_Tablesets_ICTypeRow] = obj["ICType"]
      self.ICCode:list[Erp_Tablesets_ICCodeRow] = obj["ICCode"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetCRMEnvironment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CRMEnvironmentDataTableset] = obj["returnObj"]
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

class SetCustomerAttributes_input:
   """ Required : 
   customerNumber
   attributeList
   """  
   def __init__(self, obj):
      self.customerNumber:int = obj["customerNumber"]
      """  Customer Number  """  
      self.attributeList:list[Erp_Tablesets_AttributListTableset] = obj["attributeList"]
      pass

class SetCustomerAttributes_output:
   def __init__(self, obj):
      pass

class SetCustomerIndustryCodes_input:
   """ Required : 
   customerNumber
   deleteNonListed
   industryCodeList
   """  
   def __init__(self, obj):
      self.customerNumber:int = obj["customerNumber"]
      """  Customer Number  """  
      self.deleteNonListed:bool = obj["deleteNonListed"]
      """  True to Delete any ietms not listed  """  
      self.industryCodeList:list[Erp_Tablesets_IndustryClassTableset] = obj["industryCodeList"]
      pass

class SetCustomerIndustryCodes_output:
   def __init__(self, obj):
      pass

