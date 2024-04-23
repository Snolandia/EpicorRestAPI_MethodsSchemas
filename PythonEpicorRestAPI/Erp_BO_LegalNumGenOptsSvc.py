import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LegalNumGenOptsSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumGenOptsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumGenOptsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeNumberPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeNumberPrefix
   Description: This method will update values in the LegalNumGenOpts datatable based
on the number prefix.  This method should be called when the prefix is changing.
   OperationID: ChangeNumberPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNumberPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNumberPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumGenOptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildPrefixList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildPrefixList
   OperationID: BuildPrefixList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildPrefixList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildPrefixList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumGenOptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePrompts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePrompts
   Description: This method performs validation on the legal number prompt data that
was entered.
This method will also verify the legal number entered is not already being used.
If it is, the user has the option of continuing with this number.  If the answer to
the question is no, the user will be required to enter different data.  If the answer
is yes, the user can continue with the number.
This method should be called when the user attempts to save
the data.
   OperationID: ValidatePrompts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePrompts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrompts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumGenOptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_buildDelimitedListPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method buildDelimitedListPrefix
   Description: This method returns a delimited string to populate combo
   OperationID: buildDelimitedListPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/buildDelimitedListPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/buildDelimitedListPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumGenOptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildPrefixList_input:
   """ Required : 
   ds
   whseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      self.whseCode:str = obj["whseCode"]
      pass

class BuildPrefixList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeNumberPrefix_input:
   """ Required : 
   proposedNumberPrefix
   ds
   """  
   def __init__(self, obj):
      self.proposedNumberPrefix:str = obj["proposedNumberPrefix"]
      """  The proposed prefix value  """  
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      pass

class ChangeNumberPrefix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsTableset:
   def __init__(self, obj):
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
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

class ValidatePrompts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      pass

class ValidatePrompts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumGenOptsTableset] = obj["ds"]
      self.QuestionText:str = obj["parameters"]
      pass

      """  output parameters  """  

class buildDelimitedListPrefix_input:
   """ Required : 
   delimitedList
   """  
   def __init__(self, obj):
      self.delimitedList:str = obj["delimitedList"]
      pass

class buildDelimitedListPrefix_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

