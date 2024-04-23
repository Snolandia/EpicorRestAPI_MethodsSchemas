import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMPlantSvc
# Description: Outbound integration point for Plant (Site)
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckSite
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountSite
   Description: Returns the count of existing IntQueOut records along with the count of updated sites in the database that IntQueOut records have not yet been created for
   OperationID: CountSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllSite
   Description: Generates IntQueOut and IMSite rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSite
   Description: Generates IntQueOut and IMSite rows since the last time this was called and then returns these along with any existing
   OperationID: GetSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMPlantSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckSite_input:
   """ Required : 
   IMPlantTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMPlantTableset:list[Erp_Tablesets_IMPlantTableset] = obj["IMPlantTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckSite_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class CountSite_input:
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

class CountSite_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Main phone number of the Site.  """  
      self.CommentText:str = obj["CommentText"]
      """  Comments are intended to be internal comments about a specific Site. These may get pulled into other programs. They are mainly intended as an online storage facility.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Plant has to be synchronized with Epicor FSA application.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMPlantTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMPlant:list[Erp_Tablesets_IMPlantRow] = obj["IMPlant"]
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

class GetAllSite_input:
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

class GetAllSite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMPlantTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSite_input:
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

class GetSite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMPlantTableset] = obj["returnObj"]
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

