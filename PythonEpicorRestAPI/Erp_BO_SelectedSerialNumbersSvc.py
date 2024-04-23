import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SelectedSerialNumbersSvc
# Description: New and existing serial numbers are added to the ttSelectedSerialNumbers
temp table when the user selects them.  Also allows update of the SNFormat
temp table.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AddSerialNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddSerialNum
   Description: This method is used for adding an existing SerialNo record to the Selected
Serial Numbers dataset.
   OperationID: AddSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HHScanCheckSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HHScanCheckSN
   Description: Determines whether the SN exists or not. Also performs other validation on the request.
   OperationID: HHScanCheckSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HHScanCheckSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHScanCheckSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSerialNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSerialNum
   Description: Add a serial number temporary record to the Selected Serial Number dataset.
   OperationID: CreateSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSerialNumRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSerialNumRange
   Description: Create multiple serial number temporary records in the Selected Serial Numbers dataset.
   OperationID: CreateSerialNumRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSerialNumRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSerialNumRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KineticGetSerialNumFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KineticGetSerialNumFormat
   Description: Gets the next serial number format based on the part number passed in.
   OperationID: KineticGetSerialNumFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticGetSerialNumFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticGetSerialNumFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNextSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNextSN
   Description: Gets the next serial number based on the format for the part number passed in.
   OperationID: GetNextSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNumFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNumFormat
   Description: Gets the next serial number format based on the part number passed in.
   OperationID: GetSerialNumFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNumFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveSerialNumbers
   Description: Retrieve serial numbers
   OperationID: RetrieveSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessSelectedSerialNumbers
   Description: Process selected serial numbers
   OperationID: ProcessSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSingleSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSingleSerialNumber
   Description: Add a serial number temporary record to the Selected Serial Number dataset.  The source data for this method is dataset SerialNumberSelection.
   OperationID: CreateSingleSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSingleSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSingleSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSerialNumberRange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSerialNumberRange
   Description: Create multiple serial number temporary records in the Serial Number Selection dataset.
   OperationID: CreateSerialNumberRange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSerialNumberRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSerialNumberRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNextSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNextSerialNumber
   Description: Gets the next serial number based on the format for the part number passed in.  The source
data for this method is the SerialNumberSelection dataset.
   OperationID: GetNextSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectSerialNumbers
   Description: Select/unselect all serial numbers in the SerialNumberSelection dataset.  When parameter select = true all
rows will be marked as selected; When parameter select = false all rows will be unselected.
   OperationID: SelectSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCreateSNStartAtQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCreateSNStartAtQty
   OperationID: ValidateCreateSNStartAtQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreateSNStartAtQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreateSNStartAtQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCreateSerialNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCreateSerialNumber
   OperationID: ValidateCreateSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCreateSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreateSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddSerialNum_input:
   """ Required : 
   ds
   PartNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   SerialNum
   SourceRowID
   TransType
   plantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.PartNum:str = obj["PartNum"]
      """  Part number for the serial number.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number to be added.  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID from the source transaction record.  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type from the source transaction record.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class AddSerialNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateSerialNumRange_input:
   """ Required : 
   ds
   PartNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   NumToAdd
   baseBeginNum
   SourceRowID
   TransType
   plantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.PartNum:str = obj["PartNum"]
      """  Part number for the serial number.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.NumToAdd:int = obj["NumToAdd"]
      """  Number of serial numbers to create.  """  
      self.baseBeginNum:str = obj["baseBeginNum"]
      """  The beginning base serial number.  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID from the source transaction record.  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type from the source transaction record.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class CreateSerialNumRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateSerialNum_input:
   """ Required : 
   ds
   PartNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   baseSerialNum
   SourceRowID
   transType
   plantID
   fullSerialNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.PartNum:str = obj["PartNum"]
      """  Part number for the serial number.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.baseSerialNum:str = obj["baseSerialNum"]
      """  Serial Number to be used as the base serial number.  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID from the source transaction record.  """  
      self.transType:str = obj["transType"]
      """  Transaction Type from the source transaction record.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      self.fullSerialNum:str = obj["fullSerialNum"]
      """  Full Serial Number including prefixs, suffix, subs, etc - used with generate masks  """  
      pass

class CreateSerialNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateSerialNumberRange_input:
   """ Required : 
   ds
   PartNum
   attributeSetID
   xrefPartNum
   xrefPartType
   xrefCustNum
   NumToAdd
   baseBeginNum
   SourceRowID
   TransType
   plantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.PartNum:str = obj["PartNum"]
      """  Part number for the serial number.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  ID of Attribute Set.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.NumToAdd:int = obj["NumToAdd"]
      """  Number of serial numbers to create.  """  
      self.baseBeginNum:str = obj["baseBeginNum"]
      """  The beginning base serial number.  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID from the source transaction record.  """  
      self.TransType:str = obj["TransType"]
      """  Transaction Type from the source transaction record.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class CreateSerialNumberRange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.nextBaseSN:str = obj["parameters"]
      self.snPrefix:str = obj["parameters"]
      self.nextFullSN:str = obj["parameters"]
      self.snCounterMax:bool = obj["snCounterMax"]
      self.snFormat:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateSingleSerialNumber_input:
   """ Required : 
   ds
   PartNum
   attributeSetID
   xrefPartNum
   xrefPartType
   xrefCustNum
   baseSerialNum
   SourceRowID
   transType
   plantID
   fullSerialNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.PartNum:str = obj["PartNum"]
      """  Part number for the serial number.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  ID of Attribute Set.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.baseSerialNum:str = obj["baseSerialNum"]
      """  Serial Number to be used as the base serial number.  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID from the source transaction record.  """  
      self.transType:str = obj["transType"]
      """  Transaction Type from the source transaction record.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      self.fullSerialNum:str = obj["fullSerialNum"]
      """  Full Serial Number including prefixs, suffix, subs, etc - used with generate masks  """  
      pass

class CreateSingleSerialNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class Erp_Tablesets_SelectedSerialNumbersTableset:
   def __init__(self, obj):
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialNumberSelectionRow:
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

class Erp_Tablesets_SerialNumberSelectionTableset:
   def __init__(self, obj):
      self.SerialNumberSelection:list[Erp_Tablesets_SerialNumberSelectionRow] = obj["SerialNumberSelection"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetNextSN_input:
   """ Required : 
   ds
   snPartNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   plantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.snPartNum:str = obj["snPartNum"]
      """  Part number to create serial numbers for.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class GetNextSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.nextBaseSN:str = obj["parameters"]
      self.snPrefix:str = obj["parameters"]
      self.nextFullSN:str = obj["parameters"]
      self.snCounterMax:bool = obj["snCounterMax"]
      pass

      """  output parameters  """  

class GetNextSerialNumber_input:
   """ Required : 
   ds
   snPartNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   plantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.snPartNum:str = obj["snPartNum"]
      """  Part number to create serial numbers for.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class GetNextSerialNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.nextBaseSN:str = obj["parameters"]
      self.snPrefix:str = obj["parameters"]
      self.nextFullSN:str = obj["parameters"]
      self.snCounterMax:bool = obj["snCounterMax"]
      self.snFormat:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSerialNumFormat_input:
   """ Required : 
   ds
   partNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   plantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      """  Part number to create serial numbers for.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class GetSerialNumFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HHScanCheckSN_input:
   """ Required : 
   ds
   ipPartNum
   ipXrefPartNum
   ipXrefPartType
   ipXrefCustNum
   ipBaseSerialNum
   ipSourceRowID
   ipTransType
   ipPlantID
   ipFullSerialNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part number for the serial number.  """  
      self.ipXrefPartNum:str = obj["ipXrefPartNum"]
      """  XRef Part Number.  """  
      self.ipXrefPartType:str = obj["ipXrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.ipXrefCustNum:int = obj["ipXrefCustNum"]
      """  XRef Customer Number.  """  
      self.ipBaseSerialNum:str = obj["ipBaseSerialNum"]
      """  Serial Number to be used as the base serial number.  """  
      self.ipSourceRowID:str = obj["ipSourceRowID"]
      """  RowID from the source transaction record.  """  
      self.ipTransType:str = obj["ipTransType"]
      """  Transaction Type from the source transaction record.  """  
      self.ipPlantID:str = obj["ipPlantID"]
      """  Plant associated with the transaction.  """  
      self.ipFullSerialNum:str = obj["ipFullSerialNum"]
      """  Full Serial Number including prefixs, suffix, subs, etc - used with generate masks  """  
      pass

class HHScanCheckSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      self.opSNIsDeselected:bool = obj["opSNIsDeselected"]
      self.opExists:bool = obj["opExists"]
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

class KineticGetSerialNumFormat_input:
   """ Required : 
   partNum
   xrefPartNum
   xrefPartType
   xrefCustNum
   plantID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to create serial numbers for.  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      """  XRef Part Number.  """  
      self.xrefPartType:str = obj["xrefPartType"]
      """  XRef Part Type (C=Customer/I=Internal Xref).  """  
      self.xrefCustNum:int = obj["xrefCustNum"]
      """  XRef Customer Number.  """  
      self.plantID:str = obj["plantID"]
      """  Plant associated with the transaction.  """  
      pass

class KineticGetSerialNumFormat_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.nextBaseSN:str = obj["parameters"]
      self.snPrefix:str = obj["parameters"]
      self.nextFullSN:str = obj["parameters"]
      self.snCounterMax:bool = obj["snCounterMax"]
      pass

      """  output parameters  """  

class ProcessSelectedSerialNumbers_input:
   """ Required : 
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds1"]
      pass

class ProcessSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class RetrieveSerialNumbers_input:
   """ Required : 
   whereClause
   startSerialNumber
   endSerialNumber
   forSelected
   sourceRowID
   transType
   ds
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause  """  
      self.startSerialNumber:str = obj["startSerialNumber"]
      """  Starting serial number  """  
      self.endSerialNumber:str = obj["endSerialNumber"]
      """  Ending serial number  """  
      self.forSelected:bool = obj["forSelected"]
      """  Mark retrieved as selected  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Source rowid  """  
      self.transType:str = obj["transType"]
      """  Transaction type  """  
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      pass

class RetrieveSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SelectSerialNumbers_input:
   """ Required : 
   selected
   requiredQuantity
   selectedQuantity
   ds
   """  
   def __init__(self, obj):
      self.selected:bool = obj["selected"]
      self.requiredQuantity:int = obj["requiredQuantity"]
      self.selectedQuantity:int = obj["selectedQuantity"]
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      pass

class SelectSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.deselectMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SerialNumberSelectionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCreateSNStartAtQty_input:
   """ Required : 
   startAtQty
   serialNumber
   nextFullSN
   nextBaseSN
   ds
   """  
   def __init__(self, obj):
      self.startAtQty:str = obj["startAtQty"]
      self.serialNumber:str = obj["serialNumber"]
      self.nextFullSN:str = obj["nextFullSN"]
      self.nextBaseSN:str = obj["nextBaseSN"]
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

class ValidateCreateSNStartAtQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.startAtQty:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCreateSerialNumber_input:
   """ Required : 
   serialNumber
   nextFullSN
   nextBaseSN
   ds
   """  
   def __init__(self, obj):
      self.serialNumber:str = obj["serialNumber"]
      self.nextFullSN:str = obj["nextFullSN"]
      self.nextBaseSN:str = obj["nextBaseSN"]
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

class ValidateCreateSerialNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.serialNumber:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_SelectedSerialNumbersTableset] = obj["ds"]
      pass

      """  output parameters  """  

