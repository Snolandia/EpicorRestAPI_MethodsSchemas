import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuickJobEntrySvc
# Description: Quick Job Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAttributeSetID
   Description: Call this method when the attribute set changes
   OperationID: ChangeAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuickJobEngineered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuickJobEngineered
   Description: This method validates the QuickJob.Engineered and potentially changes the Released field.
This method should run when the QuickJob.Engineered field changes.
   OperationID: ChangeQuickJobEngineered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobEngineered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobEngineered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuickJobFirm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuickJobFirm
   Description: This method validates the QuickJob.Firm and potentially changes the Released and
Engineered fields.
This method should run when the QuickJob.Firm field changes.
   OperationID: ChangeQuickJobFirm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobFirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobFirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuickJobPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuickJobPartNum
   Description: This method validates the QuickJob.PartNum and defaults fields associated with the partnum.
This method should run when the QuickJob.PartNum field changes.
   OperationID: ChangeQuickJobPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuickJobReleased(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuickJobReleased
   Description: This method validates the QuickJob.Released and potentially changes the firm and engineered fields.
This method should run when the QuickJob.Released field changes.
   OperationID: ChangeQuickJobReleased
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobReleased_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobReleased_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuickJobWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuickJobWarehouseCode
   Description: This method validates the QuickJob.WarehouseCode and defaults warehousedesc field
associated with the warehousecode.
This method should run when the QuickJob.WarehouseCode field changes.
   OperationID: ChangeQuickJobWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeQuickJobContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeQuickJobContract
   Description: Update Quick Job information with WarehouseCode from the Planning Contract
   OperationID: ChangeQuickJobContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeQuickJobContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeQuickJobContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevisionNum
   Description: Call this method when Revision changes to maintain inventory tracking
   OperationID: ChangeRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJobNum
   Description: Check if the jobnum exists
   OperationID: ValidateJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateJob
   Description: Generate the job.
   OperationID: GenerateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickJob
   Description: This method is the first thing that should be ran.  It creates a ttQuickJob record in the
dataset that we will use to collect user inputs for this Quick Job Entry process.  This method
creates the record and assigns the next job number, date, firm, released,engineered,and legal number fields
and returns the dataset with the one record.  This dataset is not a database dataset, it
is a temporary dataset with the only record ever in the dataset is the one that you create here.
   OperationID: GetNewQuickJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJobInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJobInfo
   Description: Validates Job Information before create it.
   OperationID: ValidateJobInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJobInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGenerateJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGenerateJob
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreGenerateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGenerateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGenerateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickJobEntrySvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAttributeSetID_input:
   """ Required : 
   ds
   attributeSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class ChangeAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuickJobContract_input:
   """ Required : 
   ipContractID
   ds
   """  
   def __init__(self, obj):
      self.ipContractID:str = obj["ipContractID"]
      """  The proposed ContractID  """  
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class ChangeQuickJobContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipContractID:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuickJobEngineered_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class ChangeQuickJobEngineered_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuickJobFirm_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class ChangeQuickJobFirm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuickJobPartNum_input:
   """ Required : 
   ds
   uomCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class ChangeQuickJobPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuickJobReleased_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class ChangeQuickJobReleased_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeQuickJobWarehouseCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class ChangeQuickJobWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRevisionNum_input:
   """ Required : 
   ds
   revisionNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      self.revisionNum:str = obj["revisionNum"]
      """  The new Revision number  """  
      pass

class ChangeRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
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

class Erp_Tablesets_QuickJobEntryTableset:
   def __init__(self, obj):
      self.QuickJob:list[Erp_Tablesets_QuickJobRow] = obj["QuickJob"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuickJobRow:
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      """  The Job Number  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part Number  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  The Revision Number  """  
      self.PartDesc:str = obj["PartDesc"]
      """  The description for the associated partnum.  """  
      self.Quantity:int = obj["Quantity"]
      """  The quantity for the new job  """  
      self.Firm:bool = obj["Firm"]
      """  Firm?  """  
      self.Engineered:bool = obj["Engineered"]
      """  Is the job engineered?  """  
      self.Released:bool = obj["Released"]
      """  Has the job been released?  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse code  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  The description of the warehouse  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin number  """  
      self.BinDesc:str = obj["BinDesc"]
      """  The description of the bin  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number  """  
      self.JobDate:str = obj["JobDate"]
      """  The job date field.  """  
      self.EnableEngineered:bool = obj["EnableEngineered"]
      self.EnableReleased:bool = obj["EnableReleased"]
      self.AlternateMethod:str = obj["AlternateMethod"]
      self.QuantityUOM:str = obj["QuantityUOM"]
      self.Scheduled:bool = obj["Scheduled"]
      """  Shedule a job as soon as it was created  """  
      self.ContractID:str = obj["ContractID"]
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      """  ID of related Attribute Class assigned to the Part  """  
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      """  Attribute Set Description  """  
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      """  Attribute Set Short Description  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GenerateJob_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class GenerateJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewQuickJob_input:
   """ Required : 
   ipJobNum
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      pass

class GetNewQuickJob_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuickJobEntryTableset] = obj["returnObj"]
      pass

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   sysRowID
   rowType
   uomCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.sysRowID:str = obj["sysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
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

class PreGenerateJob_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class PreGenerateJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class ValidateJobInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

class ValidateJobInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickJobEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateJobNum_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  The QuickJobEntry data set  """  
      pass

class ValidateJobNum_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

