import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlRepackReclassPCIDSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Init(epicorHeaders = None):
   """  
   Summary: Invoke method Init
   Description: for unit testing
   OperationID: Init
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSourcePCID
   Description: Sets the entered PCID as the source container if valid
   OperationID: SetSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreSetPkgControlRepackReclassPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreSetPkgControlRepackReclassPCID
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
inputs the target PCID or clicks the print button and the source qty > 0,
and before calling any update method that could generate PartTran.
   OperationID: PreSetPkgControlRepackReclassPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSetPkgControlRepackReclassPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetPkgControlRepackReclassPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RepackReclassPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RepackReclassPCID
   Description: Validates the target PCID and performs the repack based on the qty in the target PkgControlStageItem records.
   OperationID: RepackReclassPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RepackReclassPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RepackReclassPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LoadDefaultPrinter(epicorHeaders = None):
   """  
   Summary: Invoke method LoadDefaultPrinter
   Description: Loads the first active printer with the lowest DisplaySequence that is defined for the "PKG-RPK" type.
   OperationID: LoadDefaultPrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadDefaultPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ValidatePrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePrinter
   Description: Validates that the printer is active and exists for the "PKG-RPK" type.
   OperationID: ValidatePrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateNewPCIDQtyRemaining(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateNewPCIDQtyRemaining
   Description: Generates a new PCID for the remaining source PCID qty in preparation for printing the new label for the source; also updates any PkgControlSplitMerge and PkgControlStageHeader OriginalSourcePCID from old to the new PCID generated
   OperationID: GenerateNewPCIDQtyRemaining
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateNewPCIDQtyRemaining_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewPCIDQtyRemaining_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackageCodeAllocNegQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlRepackReclassPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckPackageCodeAllocNegQty_input:
   """ Required : 
   ipNewPCID
   ipPackageCode
   ipQty
   """  
   def __init__(self, obj):
      self.ipNewPCID:str = obj["ipNewPCID"]
      self.ipPackageCode:str = obj["ipPackageCode"]
      self.ipQty:int = obj["ipQty"]
      pass

class CheckPackageCodeAllocNegQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarning:str = obj["parameters"]
      self.opAction:str = obj["parameters"]
      self.opAllocWarning:str = obj["parameters"]
      self.opAllocAction:str = obj["parameters"]
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

class Erp_Tablesets_PkgControlRepackReclassPCIDRow:
   def __init__(self, obj):
      self.HasBeenPrinted:bool = obj["HasBeenPrinted"]
      """  Indicates if a new label has been printed for the source PCID after repack/reclass has taken place.  """  
      self.Seq:int = obj["Seq"]
      """  Used as the primary key for the temp table  """  
      self.SourceLPCStatus:str = obj["SourceLPCStatus"]
      """  The LPC status for the source PCID  """  
      self.SourcePCID:str = obj["SourcePCID"]
      """  The source PCID for the repack/reclass  """  
      self.SourceStatus:str = obj["SourceStatus"]
      self.SourceUOM:str = obj["SourceUOM"]
      """  UOM for the source Quantity  """  
      self.TargetPCID:str = obj["TargetPCID"]
      """  Target PCID  """  
      self.SourceQuantity:int = obj["SourceQuantity"]
      """  Total quantity of the PkgControlItem associated with the source PCID  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  Holds any message returned from the legal number generation.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse code for the transaction (comes from the source PkgControlHeader)  """  
      self.ContainerQtyMessage:str = obj["ContainerQtyMessage"]
      self.PkgCode:str = obj["PkgCode"]
      self.RemainingPCIDGenerated:bool = obj["RemainingPCIDGenerated"]
      """  Indicates if a new label has been generated for the source PCID after partial repack/reclass has taken place.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlRepackReclassPCIDTableset:
   def __init__(self, obj):
      self.PkgControlRepackReclassPCID:list[Erp_Tablesets_PkgControlRepackReclassPCIDRow] = obj["PkgControlRepackReclassPCID"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateNewPCIDQtyRemaining_input:
   """ Required : 
   ds
   printPCIDLabel
   pcidPrinter
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["ds"]
      self.printPCIDLabel:bool = obj["printPCIDLabel"]
      """  True/False indicates if the new label should be printed  """  
      self.pcidPrinter:str = obj["pcidPrinter"]
      """  User selected printer  """  
      pass

class GenerateNewPCIDQtyRemaining_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["ds"]
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

class Init_output:
   def __init__(self, obj):
      pass

class LoadDefaultPrinter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcidPrinter:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreSetPkgControlRepackReclassPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["ds"]
      pass

class PreSetPkgControlRepackReclassPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class RepackReclassPCID_input:
   """ Required : 
   ipNewPCID
   ds
   """  
   def __init__(self, obj):
      self.ipNewPCID:str = obj["ipNewPCID"]
      """  target PCID  """  
      self.ds:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["ds"]
      pass

class RepackReclassPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetSourcePCID_input:
   """ Required : 
   ipPCID
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  Source PCID  """  
      pass

class SetSourcePCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlRepackReclassPCIDTableset] = obj["returnObj"]
      pass

class ValidatePrinter_input:
   """ Required : 
   iPCIDPrinter
   """  
   def __init__(self, obj):
      self.iPCIDPrinter:str = obj["iPCIDPrinter"]
      """  User selected printer  """  
      pass

class ValidatePrinter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPCIDPrinter:str = obj["parameters"]
      pass

      """  output parameters  """  

