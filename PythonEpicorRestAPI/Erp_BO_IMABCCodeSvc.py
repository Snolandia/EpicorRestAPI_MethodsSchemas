import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMABCCodeSvc
# Description: Business Object to handle: Count, Get, Ack, Add, Update and Delete of ABCCode
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckABCCode
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountABCCode
   Description: Returns the count of existing IntQueOut records along with the count of updated abcCodes in the database that IntQueOut records have not yet been created for
   OperationID: CountABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllABCCode
   Description: Generates IntQueOut and IMABCCode rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetABCCode
   Description: Generates IntQueOut and IMABCCode rows since the last time this was called and then returns these along with any existing
   OperationID: GetABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddABCCode
   Description: Add ABCCode
   OperationID: AddABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteABCCode
   Description: Delete ABCCode
   OperationID: DeleteABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateABCCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateABCCode
   Description: Update ABCCode
   OperationID: UpdateABCCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateABCCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateABCCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMABCCodeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckABCCode_input:
   """ Required : 
   IMABCCodeTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMABCCodeTableset:list[Erp_Tablesets_IMABCCodeTableset] = obj["IMABCCodeTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckABCCode_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class AddABCCode_input:
   """ Required : 
   IMABCCodeTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   saveAddOnError
   imIntegrationKey
   """  
   def __init__(self, obj):
      self.IMABCCodeTableset:list[Erp_Tablesets_IMABCCodeTableset] = obj["IMABCCodeTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.saveAddOnError:bool = obj["saveAddOnError"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

class AddABCCode_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

      """  output parameters  """  

class CountABCCode_input:
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

class CountABCCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteABCCode_input:
   """ Required : 
   IMABCCodeTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMABCCodeTableset:list[Erp_Tablesets_IMABCCodeTableset] = obj["IMABCCodeTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class DeleteABCCode_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMABCCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.CountFreq:int = obj["CountFreq"]
      """  Indicates how often parts in the classification are to be counted expressed in number of days  """  
      self.ExcludeFromCC:bool = obj["ExcludeFromCC"]
      """  This flag is set to true prevent items that should only be counted during physical inventory from being selected for cycle counting. This setting can be overridden in SiteConfABC and/or WarehseABC.  """  
      self.StockValPcnt:int = obj["StockValPcnt"]
      """  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting can be overridden in SiteConfABC and/or WarehseABC.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC. Zero indicates that any quantity variance is considered out  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC. Zero indicates that any quantity variance is consid  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, WarehseABC or SiteConfABC  An entry of zero will indicate that any value variance will be con  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMABCCodeTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMABCCode:list[Erp_Tablesets_IMABCCodeRow] = obj["IMABCCode"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMIntegrationKeyRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      """  The master file which the integration is related to.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMIntegrationKeyTableset:
   def __init__(self, obj):
      self.IMIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyRow] = obj["IMIntegrationKey"]
      self.IMNaturalKeys:list[Erp_Tablesets_IMNaturalKeysRow] = obj["IMNaturalKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMNaturalKeysRow:
   def __init__(self, obj):
      self.KeyValue:str = obj["KeyValue"]
      self.KeyColumn:str = obj["KeyColumn"]
      self.Sequence:int = obj["Sequence"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.SysRowID:str = obj["SysRowID"]
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

class GetABCCode_input:
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

class GetABCCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMABCCodeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetAllABCCode_input:
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

class GetAllABCCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMABCCodeTableset] = obj["returnObj"]
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

class UpdateABCCode_input:
   """ Required : 
   IMABCCodeTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMABCCodeTableset:list[Erp_Tablesets_IMABCCodeTableset] = obj["IMABCCodeTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class UpdateABCCode_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

