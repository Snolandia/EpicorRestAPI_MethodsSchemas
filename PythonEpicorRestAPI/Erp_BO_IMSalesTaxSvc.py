import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMSalesTaxSvc
# Description: Outbound integration point for SalesTax, SalesTRC, TaxRate
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMSalesTaxSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMSalesTaxSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckSalesTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckSalesTax
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSalesTaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountSalesTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountSalesTax
   Description: Returns the count of existing IntQueOut records along with the count of updated SalesTax in the database that IntQueOut records have not yet been created for
   OperationID: CountSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSalesTaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllSalesTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllSalesTax
   Description: Generates IntQueOut and IMSalesTax rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSalesTaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesTax
   Description: Generates IntQueOut and IMSalesTax rows since the last time this was called and then returns these along with any existing
   OperationID: GetSalesTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMSalesTaxSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckSalesTax_input:
   """ Required : 
   ts
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_IMSalesTaxTableset] = obj["ts"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckSalesTax_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class CountSalesTax_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class CountSalesTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMSalesTRCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMSalesTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Full description for a  Sales Tax master.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the tax type has to be synchronized with Epicor FSA application.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMSalesTaxTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMSalesTax:list[Erp_Tablesets_IMSalesTaxRow] = obj["IMSalesTax"]
      self.IMSalesTRC:list[Erp_Tablesets_IMSalesTRCRow] = obj["IMSalesTRC"]
      self.IMTaxRate:list[Erp_Tablesets_IMTaxRateRow] = obj["IMTaxRate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMTaxRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  First date tax rate is valid for  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllSalesTax_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetAllSalesTax_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMSalesTaxTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSalesTax_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetSalesTax_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMSalesTaxTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

