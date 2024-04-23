import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfiguratorCodeEditorSvc
# Description: Configurator code editor service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BuildCodeEditorOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildCodeEditorOptions
   Description: retrieves the Available Options for the code editor
   OperationID: BuildCodeEditorOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildCodeEditorOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildCodeEditorOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConfiguratorCodeEditor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConfiguratorCodeEditor
   Description: get a new parameters row
   OperationID: GetNewConfiguratorCodeEditor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConfiguratorCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConfiguratorCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorCodeEditorSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BuildCodeEditorOptions_input:
   """ Required : 
   codeLanguage
   ConfiguratorCodeEditorTS
   """  
   def __init__(self, obj):
      self.codeLanguage:str = obj["codeLanguage"]
      """  The code language to construct the code editor  """  
      self.ConfiguratorCodeEditorTS:list[Erp_Tablesets_ConfiguratorCodeEditorTableset] = obj["ConfiguratorCodeEditorTS"]
      pass

class BuildCodeEditorOptions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ConfiguratorCodeEditorTS:list[Erp_Tablesets_ConfiguratorCodeEditorTableset] = obj["ConfiguratorCodeEditorTS"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CodeEditorPCFuncParamRow:
   def __init__(self, obj):
      self.ParameterName:str = obj["ParameterName"]
      self.ParameterType:str = obj["ParameterType"]
      self.Modifier:str = obj["Modifier"]
      self.DefaultValue:str = obj["DefaultValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCInputsRow:
   def __init__(self, obj):
      self.InputName:str = obj["InputName"]
      self.InputType:str = obj["InputType"]
      self.DataType:str = obj["DataType"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfigUDCodEditorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.FunctionName:str = obj["FunctionName"]
      self.MethodDeclaration:str = obj["MethodDeclaration"]
      self.MethodToolTip:str = obj["MethodToolTip"]
      self.DataType:str = obj["DataType"]
      self.TokenizedText:str = obj["TokenizedText"]
      """  The tokenized text used for the expression builder.  """  
      self.MethodType:str = obj["MethodType"]
      self.CodeEditorText:str = obj["CodeEditorText"]
      self.ExcludeFromExpressionBuilder:bool = obj["ExcludeFromExpressionBuilder"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfiguratorCodeEditorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.RetrieveExpVars:bool = obj["RetrieveExpVars"]
      self.UDMethodFunctionType:str = obj["UDMethodFunctionType"]
      """   None -> do not retrieve UD Methods (string.empty = none)
Both -> retrieve client and server
Client -> retrieve client only
Server -> retrieve server only  """  
      self.FromUDMethods:bool = obj["FromUDMethods"]
      self.DedicatedTenancy:bool = obj["DedicatedTenancy"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfiguratorCodeEditorTableset:
   def __init__(self, obj):
      self.ConfiguratorCodeEditor:list[Erp_Tablesets_ConfiguratorCodeEditorRow] = obj["ConfiguratorCodeEditor"]
      self.CodeEditorPCFuncParam:list[Erp_Tablesets_CodeEditorPCFuncParamRow] = obj["CodeEditorPCFuncParam"]
      self.CodeEditorPCInputs:list[Erp_Tablesets_CodeEditorPCInputsRow] = obj["CodeEditorPCInputs"]
      self.ConfigUDCodEditor:list[Erp_Tablesets_ConfigUDCodEditorRow] = obj["ConfigUDCodEditor"]
      self.PcExpVar:list[Erp_Tablesets_PcExpVarRow] = obj["PcExpVar"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcExpVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TokenizedText:str = obj["TokenizedText"]
      """  Tokenized Text used by the expression builder.  """  
      self.CodeEditorText:str = obj["CodeEditorText"]
      self.AlternateText:str = obj["AlternateText"]
      self.Approved:bool = obj["Approved"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetNewConfiguratorCodeEditor_input:
   """ Required : 
   companyID
   configID
   ConfiguratorCodeEditorTS
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      """  Company ID  """  
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.ConfiguratorCodeEditorTS:list[Erp_Tablesets_ConfiguratorCodeEditorTableset] = obj["ConfiguratorCodeEditorTS"]
      pass

class GetNewConfiguratorCodeEditor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ConfiguratorCodeEditorTS:list[Erp_Tablesets_ConfiguratorCodeEditorTableset] = obj["ConfiguratorCodeEditorTS"]
      pass

      """  output parameters  """  

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

