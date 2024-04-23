import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMFSWarrCdSvc
# Description: Business Object to handle: Count, Get, Ack, and GetAll of FSWarrCd
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMFSWarrCdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMFSWarrCdSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckFSWarrCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckFSWarrCd
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckFSWarrCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckFSWarrCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckFSWarrCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSWarrCdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountFSWarrCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountFSWarrCd
   Description: Returns the count of existing IntQueOut records along with the count of updated FSWarrCd in the database that IntQueOut records have not yet been created for
   OperationID: CountFSWarrCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountFSWarrCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountFSWarrCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSWarrCdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllFSWarrCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllFSWarrCd
   Description: Generates IntQueOut and IMFSWarrCd rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllFSWarrCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllFSWarrCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllFSWarrCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSWarrCdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFSWarrCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFSWarrCd
   Description: Generates IntQueOut and IMFSWarrCd rows since the last time this was called and then returns these along with any existing
   OperationID: GetFSWarrCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFSWarrCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSWarrCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSWarrCdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckFSWarrCd_input:
   """ Required : 
   ts
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_IMFSWarrCdTableset] = obj["ts"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckFSWarrCd_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class CountFSWarrCd_input:
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

class CountFSWarrCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMFSWarrCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique identifer of the warranty assigned by the user.  """  
      self.WarrDescription:str = obj["WarrDescription"]
      """  Description of the warranty.  """  
      self.MaterialDuration:int = obj["MaterialDuration"]
      """  The number of days, months, or years the material is covered by the warranty if FSWarrCD.MatCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.LaborDuration:int = obj["LaborDuration"]
      """  The number of days, months, or years the Labor is covered by the warranty if FSWarrCd.LabCovered = True. FSWarrCd.LaborMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MiscDuration:int = obj["MiscDuration"]
      """  The number of days, months, or years the Misc Charges are covered by the warranty if FSWarrCd.MiscCovered = True. FSWarrCd.MiscMod contains the weeks, months, years modifier of the value entered in this field.  """  
      self.MaterialMod:str = obj["MaterialMod"]
      """  Determines whether the FSWarrCd.MaterialDuration value is in days, months or years.  """  
      self.LaborMod:str = obj["LaborMod"]
      """  Determines whether the FSWarrCd.LaborDuration value is in days, months or years.  """  
      self.MiscMod:str = obj["MiscMod"]
      """  Determines whether the FSWarrCd.MiscDuration value is in days, months or years.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments about the Warranty. These will print on the Sales Order Acknowledgement Form when a part that is associated with this Warranty appears on the order.  """  
      self.OnSite:bool = obj["OnSite"]
      """  Determines whether or not the Warranty covers onsite visits.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Determines whether or not material costs are covered by the warranty.  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Determines whether labor costs are covered by the warranty.  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Determines whether or not Miscellaneous costs are covered by the warranty.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warranty has to be synchronized with Epicor FSA application.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSWarrCdTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMFSWarrCd:list[Erp_Tablesets_IMFSWarrCdRow] = obj["IMFSWarrCd"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class GetAllFSWarrCd_input:
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

class GetAllFSWarrCd_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMFSWarrCdTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetFSWarrCd_input:
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

class GetFSWarrCd_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMFSWarrCdTableset] = obj["returnObj"]
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

