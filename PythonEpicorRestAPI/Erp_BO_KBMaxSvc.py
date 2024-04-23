import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.KBMaxSvc
# Description: CPQ Library
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Login(epicorHeaders = None):
   """  
   Summary: Invoke method Login
   Description: Login to the CPQ Instance
   OperationID: Login
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Login_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetKBMaxAttachmentDocTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetKBMaxAttachmentDocTypeList
   Description: Get the list of valid Attachment Document Types specific for CPQ.
List will contain Doc Types that are not specific to table, and Doc Types that are specific QuoteDtl, QuoteAsm, OrderDtl, JobHead, JobAsmbl.
   OperationID: GetKBMaxAttachmentDocTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKBMaxAttachmentDocTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetConfigurator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConfigurator
   Description: Get the CPQ Configurator Product ID from a Kinetic Configurator
and validate it can be used.
   OperationID: GetConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetConfiguredProduct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetConfiguredProduct
   Description: Validate entity table and get CPQ Configured Product.
   OperationID: GetConfiguredProduct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetConfiguredProduct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetConfiguredProduct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCanSave(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCanSave
   Description: Checks if CPQ configuration has any validation errors and if so validates if it can be saved.
   OperationID: ValidateCanSave
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCanSave_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCanSave_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCanSave(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCanSave
   Description: Checks if CPQ configuration has any validation errors and if so validates if it can be saved.
   OperationID: CheckCanSave
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCanSave_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCanSave_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddAttachments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddAttachments
   Description: Method to upload file to the storage defined by CPQ Document Type
   OperationID: AddAttachments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddAttachments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddAttachments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DocumentRulesEntitySchema(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DocumentRulesEntitySchema
   Description: Returns schema for doc rules specific for CPQ
   OperationID: DocumentRulesEntitySchema
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocumentRulesEntitySchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocumentRulesEntitySchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KBMaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddAttachments_input:
   """ Required : 
   configID
   fileName
   data
   metadata
   """  
   def __init__(self, obj):
      self.configID:int = obj["configID"]
      self.fileName:str = obj["fileName"]
      self.data:str = obj["data"]
      self.metadata      #schema had no properties on an object.
      pass

class AddAttachments_output:
   def __init__(self, obj):
      pass

class CheckCanSave_input:
   """ Required : 
   configuredProductJson
   """  
   def __init__(self, obj):
      self.configuredProductJson:str = obj["configuredProductJson"]
      pass

class CheckCanSave_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.canSave:bool = obj["canSave"]
      self.canSaveError:str = obj["parameters"]
      pass

      """  output parameters  """  

class DocumentRulesEntitySchema_input:
   """ Required : 
   kbConfigID
   """  
   def __init__(self, obj):
      self.kbConfigID:int = obj["kbConfigID"]
      pass

class DocumentRulesEntitySchema_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_KBMaxTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_KBMaxDocRulesColumnsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company indicator  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Column Name  """  
      self.ColumnSyntax:str = obj["ColumnSyntax"]
      """  Full column name.  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.UDColumn:bool = obj["UDColumn"]
      """  Indicate if this field is a UD Field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_KBMaxDocRulesTablesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company indicator  """  
      self.TableName:str = obj["TableName"]
      """  Table name.  """  
      self.Description:str = obj["Description"]
      """  Table description  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_KBMaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company indicator  """  
      self.KBConfigID:int = obj["KBConfigID"]
      """  CPQ Configurator ID  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AllowAttributes:bool = obj["AllowAttributes"]
      """  Attributes are allowed to be used in configuration  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_KBMaxTableset:
   def __init__(self, obj):
      self.KBMax:list[Erp_Tablesets_KBMaxRow] = obj["KBMax"]
      self.KBMaxDocRulesTables:list[Erp_Tablesets_KBMaxDocRulesTablesRow] = obj["KBMaxDocRulesTables"]
      self.KBMaxDocRulesColumns:list[Erp_Tablesets_KBMaxDocRulesColumnsRow] = obj["KBMaxDocRulesColumns"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetConfigurator_input:
   """ Required : 
   configID
   validate
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configurator ID  """  
      self.validate:bool = obj["validate"]
      """  Whether to perform validation  """  
      pass

class GetConfigurator_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  CPQ Configurator ID  """  
      pass

class GetConfiguredProduct_input:
   """ Required : 
   kbConfigProdID
   entityTable
   """  
   def __init__(self, obj):
      self.kbConfigProdID:int = obj["kbConfigProdID"]
      self.entityTable:str = obj["entityTable"]
      pass

class GetConfiguredProduct_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  CPQ Configured Product  """  
      pass

class GetKBMaxAttachmentDocTypeList_output:
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

class Login_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.url:str = obj["parameters"]
      self.authCookie:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateCanSave_input:
   """ Required : 
   configuredProductJson
   """  
   def __init__(self, obj):
      self.configuredProductJson:str = obj["configuredProductJson"]
      pass

class ValidateCanSave_output:
   def __init__(self, obj):
      pass

